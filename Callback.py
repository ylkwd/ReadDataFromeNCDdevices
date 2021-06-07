# TODO the NCDEnterprise library requires the digi Xbee library from:
# https://github.com/digidotcom/python-xbee
import re
from ncd_enterprise import NCDEnterprise
import datetime
import Database
import mysql
from mysql.connector import errors

# TODO Change this line to yours
# conn = pymysql.connect (host='127.0.0.1',user='root',password ='1234',db=,,charset='utf8')
SERIAL_PORT = "COM3"
BAUD_RATE = 115200
# print('Running')
#
conn = Database.connect_database()


#
#
# Database.create_table(conn)


# Function
now = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
sensorlist = [now]
count = 0

def my_custom_callback(sensor_data):
    print('succesful callback')
    # print('full return: '+str(sensor_data))
    print('Running')
    # now = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    for prop in sensor_data:
        # print(prop + ' ' + str(sensor_data[prop]))
        # print('')

        # About Motor 1
        # if sensor_data['sensor_type_id'] == 12 and sensor_data['source_address'] == str("0013A20041D20683"):
        if sensor_data['source_address'] == str("0013A20041D20683"):
            # csv_file = open('current_data_1.csv', 'a+')
            # csv_file.write(now + ',' + str(sensor_data['source_address']) + ',' + str(
            #     sensor_data['sensor_data']) + ',' + str(sensor_data['battery_percent']) + '\n')
            # csv_file.write(str(sensor_data[prop]) + '\n')
            # print(str(sensor_data['battery_percent'][:2]))
            print("0683")
            list0 = data_mysql(now, sensor_data)
            # Database.insert_data_vib(conn, list0,"motor2_vib")
            # csv_file.close()
            # print(list0)
            #testing

        elif sensor_data['source_address'] == str("0013A20041D63E83"):
            # csv_file = open('motor1_vib.csv', 'a+')
            # csv_file.write(now + ',' + str(sensor_data['source_address']) + ',' + str(
            #     sensor_data['sensor_data']) + ',' + str(sensor_data['battery_percent']) + '\n')
            # csv_file.write(str(sensor_data[prop]) + '\n')
            # csv_file.close()
            datalist = re.split(': |, ', str(sensor_data['sensor_data']))
            # print(str(sensor_data['battery_percent'].format()))

            sensorlist1 = [now]

            # print(sensor_data)
            #
            # print(str(sensor_data['nodeId']))
            # print(str(sensor_data['firmware']))
            # print(str(sensor_data['battery_percent']))
            # print(str(sensor_data['counter']))
            # print(str(sensor_data['source_address']))
            # print(str(sensor_data['sensor_data']['channel_1']))
            # print(str(sensor_data['sensor_data']['channel_2']))
            # print(str(sensor_data['sensor_data']['channel_3']))

            append_data(sensorlist1, str(sensor_data['battery_percent'][0:4]))
            append_data(sensorlist1, str(sensor_data['source_address']))
            append_data(sensorlist1, str(sensor_data['sensor_data']['channel_1']))
            append_data(sensorlist1, str(sensor_data['sensor_data']['channel_2']))
            append_data(sensorlist1, str(sensor_data['sensor_data']['channel_3']))

            # print(sensorlist)
            print("3E83")
            # list = data_mysql(now, sensor_data)
            # Database.insert_data_cur(conn, sensorlist1,"motor1_cur")

        elif sensor_data['source_address'] == str("0013A20041D2067A"):
            datalist = re.split(': |, ', str(sensor_data['sensor_data']))
            print("067A")
            # sensorlist = [now]

            # print(sensor_data)
            #
            # print(str(sensor_data['nodeId']))
            # print(str(sensor_data['firmware']))
            # print(str(sensor_data['battery_percent']))
            # print(str(sensor_data['counter']))
            # print(str(sensor_data['source_address']))
            # print(str(sensor_data['sensor_data']['rms_x']))
            # print(str(sensor_data['sensor_data']['rms_y']))
            # print(str(sensor_data['sensor_data']['rms_z']))
            # print(str(sensor_data['sensor_data']['max_x']))
            # print(str(sensor_data['sensor_data']['max_y']))
            # print(str(sensor_data['sensor_data']['max_z']))
            # print(str(sensor_data['sensor_data']['min_x']))
            # print(str(sensor_data['sensor_data']['min_y']))
            # print(str(sensor_data['sensor_data']['min_z']))
            # print(str(sensor_data['sensor_data']['temperature']))

            append_data(sensorlist, str(sensor_data['battery_percent'][0:4]))
            append_data(sensorlist, str(sensor_data['source_address']))
            append_data(sensorlist, str(sensor_data['sensor_data']['rms_x']))
            append_data(sensorlist, str(sensor_data['sensor_data']['rms_y']))
            append_data(sensorlist, str(sensor_data['sensor_data']['rms_z']))
            append_data(sensorlist, str(sensor_data['sensor_data']['max_x']))
            append_data(sensorlist, str(sensor_data['sensor_data']['max_y']))
            append_data(sensorlist, str(sensor_data['sensor_data']['max_z']))
            append_data(sensorlist, str(sensor_data['sensor_data']['min_x']))
            append_data(sensorlist, str(sensor_data['sensor_data']['min_y']))
            append_data(sensorlist, str(sensor_data['sensor_data']['min_z']))
            append_data(sensorlist, str(sensor_data['sensor_data']['temperature']))

    #       print(sensorlist)


            Database.insert_data_vib(conn, sensorlist, "motor1_vib")



    # print(str(sensor_data['battery_percent']))
    # print(sensorlist)
        # print(list)
    # exit()
    #


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


def append_data(sensorlist, sensor_data):
    sensorlist.append(sensor_data)
    # print(sensorlist)


def data_mysql(time, sensor_data):
    count = 0
    sensorlist = [time]
    datalist = re.split(': |, |}}|{|\s ', str(sensor_data))
    # print(sensor_data)
    count1 = 0
    # print(datalist)
    for x in datalist:
        # print(x)
        if count % 2 == 0 and count != 18 and count != 0:
            # print(x)
            # print(count)
            sensorlist.append(x)
            # print(sensorlist)
            # print(count1)
            count1 = count1 + 1
        count = count + 1
    # print('\n')
    # print(sensorlist[0])
    # print(sensorlist[1])
    # print(sensorlist[2])
    # print(sensorlist[4])
    # print(sensorlist[5])
    # print(sensorlist[7])
    # print(sensorlist[9])
    # print(sensorlist[10])
    # print(sensorlist[11])
    # print(sensorlist[12])
    # print(sensorlist[13])
    # print(sensorlist[14])
    # print(sensorlist[15])
    # print(sensorlist[16])
    # print(sensorlist[17])
    # print(sensorlist[18])
    # print(sensorlist)
    return sensorlist


# Error callbacks are only supported for the vibration time series data sets currently
def error_callback(error_data):
    print('Error detected:')
    print(error_data)


# instantiate the NCDEnterprise Object and pass in the Serial Port, Baud Rate,
# and Function/Method object
# the error handler method MUST be keyed as error_handler.
ncdModem = NCDEnterprise(SERIAL_PORT, BAUD_RATE, my_custom_callback, {'error_handler': error_callback})

print(ncdModem.device.serial_port.rts)


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
