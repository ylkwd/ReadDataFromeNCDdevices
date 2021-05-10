from ncd_enterprise import NCDEnterprise
import datetime
import pandas as pd

SERIAL_PORT = "COM3"
BAUD_RATE = 115200


# Function
def my_custom_callback(sensor_data):
    print('Running')
    now = datetime.datetime.now()

    for prop in sensor_data:
        print(prop + ' ' + str(sensor_data[prop]))
        print('1')

        # About Motor 1
        if sensor_data['sensor_type_id'] == 13 and sensor_data['source_address'] == str("0013A20041C4D793"):
            print(now.strftime("%y-%m-%d %H:%M:%S") + ',' + str(sensor_data['source_address']) + ',' + str(
                sensor_data['sensor_data']) + ',' + str(sensor_data['battery_percent']) + '\n')
            # df = pd.DataFrame([[now.strftime("%y-%m-%d %H:%M:%S"),str(sensor_data['source_address'],str(sensor_data['sensor_data']),str(sensor_data['battery_percent'])+'\n')],
            #    columns=['Time', 'Address', 'data', 'Battery','1'])
            # df.to_csv('current_data_1.csv', index=False, encoding='cp949')

        elif sensor_data['sensor_type_id'] == 40 and sensor_data['source_address'] == str("0013A20041D2067A"):
            print(now.strftime("%y-%m-%d %H:%M:%S") + ',' + str(sensor_data['source_address']) + ',' + str(
                sensor_data['sensor_data']) + ',' + str(sensor_data['battery_percent']) + '\n')
            # df = pd.DataFrame([[now.strftime("%y-%m-%d %H:%M:%S"),str(sensor_data['source_address'],str(sensor_data['sensor_data']),str(sensor_data['battery_percent'])+'\n')],
            #    columns=['Time', 'Address', 'data', 'Battery'])
            # df.to_csv('vibration_data_1.csv', index=False, encoding='cp949')
            # csv_file.close()

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


def error_callback(error_data):
    print('Error detected:')
    print(error_data)


ncdModem = NCDEnterprise(SERIAL_PORT, BAUD_RATE, my_custom_callback, {'error_handler': error_callback})


def restructure_data(data):
    r_data = {'rms_x_csv': '\"RMS_X\",', 'rms_y_csv': '\"RMS_Y\",', 'rms_z_csv': '\"RMS_Z\",',
              'temperature_csv': '\"temperature\,', 'amps_csv': '\"amps\,'}
    for sample in data:
        r_data['rms_x_csv'] += '\"' + str(data.get(sample)['rms_x']) + '\",'
        r_data['rms_y_csv'] += '\"' + str(data.get(sample)['rms_y']) + '\",'
        r_data['rms_z_csv'] += '\"' + str(data.get(sample)['rms_z']) + '\",'
        r_data['temperature_csv'] += '\"' + str(data.get(sample)['temperature']) + '\",'
        r_data['amps_csv'] += '\"' + str(data.get(sample)['amps']) + '\",'

    return r_data
