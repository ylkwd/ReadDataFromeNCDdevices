import mysql.connector
from mysql.connector import errorcode
import datetime


def connect_database():
    try:
        cnx = mysql.connector.connect(user='root',
                                      password='123456789',
                                      database='mando',
                                      host='127.0.0.1',
                                      auth_plugin='mysql_native_password')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print("error")
            print(err)
    else:
        print("connected")
        return cnx
        # for x in mycursor:
        #     print(x)


def create_table_cur(conn, table_name):
    mycursor = conn.cursor()
    mycursor.execute("DROP TABLE IF EXISTS {table_name}".format(table_name=table_name))
    sql = """CREATE TABLE IF NOT EXISTS {table_name} (Id INT AUTO_INCREMENT PRIMARY KEY,
        time VARCHAR(255),
        nodeId VARCHAR(255),
        firmware VARCHAR(255),
        Battery VARCHAR(255),
        counter VARCHAR(255),
        source_address VARCHAR(255),
        I_a VARCHAR(255),
        I_b VARCHAR(255),
        I_c VARCHAR(255))"""
    mycursor.execute(sql.format(table_name=table_name))
    # mycursor.execute(
    #     )
    # mycursor.execute("CREATE TABLE customers")
    print("Table is created")


def create_table_vib(conn, table_name):
    mycursor = conn.cursor()
    mycursor.execute("DROP TABLE IF EXISTS {table_name}".format(table_name=table_name))
    sql = """CREATE TABLE IF NOT EXISTS {table_name} (Id INT AUTO_INCREMENT PRIMARY KEY,
        time VARCHAR(255),
        nodeId VARCHAR(255), 
        firmware VARCHAR(255),
        Battery VARCHAR(255),
        counter VARCHAR(255),
        source_address VARCHAR(255),
        rms_x VARCHAR(255),
        rms_y VARCHAR(255),
        rms_z VARCHAR(255),
        max_x VARCHAR(255),
        max_y VARCHAR(255),
        max_z VARCHAR(255),
        min_x VARCHAR(255),
        min_y VARCHAR(255),
        min_z VARCHAR(255),
        temperature VARCHAR(255))"""
    mycursor.execute(sql.format(table_name=table_name))
    # mycursor.execute(
    #     )
    # mycursor.execute("CREATE TABLE customers")
    print("Table is created")


def insert_data_cur(conn, motor1_cur,table_name):
    now = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    mycursor = conn.cursor()
    sql = """INSERT INTO {table_name}
        (time,nodeId,firmware,Battery, 
        counter, source_address, I_a, I_b, I_c)
         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    value = (motor1_cur[0], motor1_cur[1], motor1_cur[2], motor1_cur[3],
             motor1_cur[4],
             motor1_cur[5], motor1_cur[6], motor1_cur[7], motor1_cur[8])
    try:
        mycursor.execute(sql.format(table_name=table_name), value)
        conn.commit()
        print("Cur "+ table_name +" inserted " + now)
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)


def insert_data_vib(conn, motor1_vib,table_name):
    now = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    mycursor = conn.cursor()
    sql = """INSERT INTO {table_name}
        (time,nodeId,firmware,Battery, 
        counter, source_address, rms_x, rms_y,
         rms_z, max_x, max_y, max_z,
          min_x, min_y, min_z, temperature)
         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    value = (motor1_vib[0], motor1_vib[1], motor1_vib[2], motor1_vib[4][1:5],
             motor1_vib[5], motor1_vib[7], motor1_vib[9], motor1_vib[10],
             motor1_vib[11], motor1_vib[12], motor1_vib[13], motor1_vib[14],
             motor1_vib[15], motor1_vib[16], motor1_vib[17], motor1_vib[18])
    try:
        mycursor.execute(sql.format(table_name=table_name), value)
        conn.commit()
        print("Vib "+ table_name +" inserted " + now)
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)


# conn = connect_database()
# create_table_vib(conn, "motor2_vib")
# create_table_vib(conn, "motor1_vib")
#
#
# create_table_cur(conn, "motor1_cur")
# insert_data(conn)
