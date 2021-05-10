from ncd_enterprise import NCDEnterprise
import datetime
import pyodbc
    
SERIAL_PORT = "COM3"
BAUD_RATE = 115200
conn = pyodbc.connect(
    "Driver={SQL server Native Client 11.0};"
    "server=DESKTOP-A4VHACS;"
    "Database=mando;"
    "Trusted_connection=yes;"
)
print('Connect DB')

conn.close()
#Function
def my_custom_callback(sensor_data):
    now = datetime.datetime.now()
    for prop in sensor_data:
        # About Motor 1
        if sensor_data['sensor_type_id'] == 12 and sensor_data['source_address'] == str("0013A20041C4D793"):
            # csv_file = open('current_data_1.csv', 'a+')
            # csv_file.write(now.strftime("%y-%m-%d %H:%M:%S")+','+str(sensor_data['source_address'])+','+str(sensor_data['sensor_data'])+','+str(sensor_data['battery_percent'])+'\n')
            # csv_file.write(str(sensor_data[prop])+'\n')
            # csv_file.close()
            print(now.strftime("%y%m%d %H:%M:%S")+','+str(sensor_data['source_address'])+','+str(sensor_data['sensor_data'])+','+str(sensor_data['battery_percent'])+'\n')
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO mando.dbo.Motor1_Current(Time, Address, channel_1, channel_2, channel_3, Battery)
            OUTPUT Inserted.Time, Inserted.Address, Inserted.channel_1, Inserted.channel_2, Inserted.channel_3
            VALUES ('Alan', '30', 'London')
            """)
            for row in cursor:
            conn.commit()
            conn.close()
            
        elif sensor_data['sensor_type_id'] == 40 and sensor_data['source_address'] == str("0013A20041D2067A"):
            # csv_file = open('vibration_data_1.csv', 'a+')
            # csv_file.write(now.strftime("%y-%m-%d %H:%M:%S")+','+str(sensor_data['source_address'])+','+str(sensor_data['sensor_data'])+','+str(sensor_data['battery_percent'])+'\n')
            # csv_file.write(str(sensor_data[prop])+'\n')
            # csv_file.close()
            print(now.strftime("%y%m%d %H:%M:%S")+','+str(sensor_data['source_address'])+','+str(sensor_data['sensor_data'])+','+str(sensor_data['battery_percent'])+'\n')
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO mando.dbo.Motor1_Vibration(Time, Address, rms_x, rms_y, rms_z, min_x, min_y, min_z, max_x, max_y, max_z, temperature, Battery)
            OUTPUT Inserted.Time, Inserted.Address, Inserted.rms_x, Inserted.rms_y, Inserted.rms_z, Inserted.min_x, Inserted.min_y, Inserted.min_z, Inserted.max_x, Inserted.max_y, Inserted.max_z, Inserted.temperature, Inserted.Battery
            VALUES ('Alan', '30', 'London')
            """)
            for row in cursor:
            print(row)
            conn.commit()
            conn.close()

        ## About Motor 2    
        # elif sensor_data['sensor_type_id'] == 13 and sensor_data['source_address'] == str("TODO"):
        #     csv_file = open('current_data_2.csv', 'a+')
        #     csv_file.write(str(sensor_data[prop])+'\n')
        #     csv_file.close()
        # elif sensor_data['sensor_type_id'] == 40 and sensor_data['source_address'] == str("TODO"):
        #     csv_file = open('vibration_data_2.csv', 'a+')
        #     csv_file.write(str(sensor_data[prop])+'\n')
        #     csv_file.close()

        ## About Motor 3
        # elif sensor_data['sensor_type_id'] == 13 and sensor_data['source_address'] == str("TODO"):
        #     csv_file = open('current_data_3.csv', 'a+')
        #     csv_file.write(str(sensor_data[prop])+'\n')
        #     csv_file.close()
        # elif sensor_data['sensor_type_id'] == 40 and sensor_data['source_address'] == str("TODO"):
        #     csv_file = open('vibration_data_3.csv', 'a+')
        #     csv_file.write(str(sensor_data[prop])+'\n')
        #     csv_file.close()
    
# Error callbacks are only supported for the vibration time series data sets currently
def error_callback(error_data):
    print('Error detected:')
    print(error_data)

#instantiate the NCDEnterprise Object and pass in the Serial Port, Baud Rate,
# and Function/Method object
# the error handler method MUST be keyed as error_handler.
ncdModem = NCDEnterprise(SERIAL_PORT, BAUD_RATE, my_custom_callback, {'error_handler': error_callback})
# print(ncdModem.device.serial_port.rts)

def restructure_data(data):
    r_data = {'rms_x_csv': '\"RMS_X\",', 'rms_y_csv': '\"RMS_Y\",', 'rms_z_csv': '\"RMS_Z\",', 'temperature_csv': '\"temperature\,', 'amps_csv': '\"amps\,'}
    for sample in data:
        r_data['rms_x_csv'] += '\"'+str(data.get(sample)['rms_x']) +'\",'
        r_data['rms_y_csv'] += '\"'+str(data.get(sample)['rms_y']) +'\",'
        r_data['rms_z_csv'] += '\"'+str(data.get(sample)['rms_z']) +'\",'
        r_data['temperature_csv'] += '\"'+str(data.get(sample)['temperature']) +'\",'
        r_data['amps_csv'] += '\"'+str(data.get(sample)['amps']) +'\",'

    return r_data
