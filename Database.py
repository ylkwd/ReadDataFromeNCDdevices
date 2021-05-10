import mysql.connector
from mysql.connector import errorcode
import datetime

def connect_database():
    try:
        cnx = mysql.connector.connect(user='root',
                                      password='123456',
                                      database='ncd',
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


def create_table(conn):
    mycursor = conn.cursor()
    mycursor.execute("DROP TABLE IF EXISTS data")
    sql = """CREATE TABLE IF NOT EXISTS data (Id INT AUTO_INCREMENT PRIMARY KEY,
        time VARCHAR(255),
        nodeId VARCHAR(255), 
        firmware VARCHAR(255),
        battery_percent VARCHAR(255),
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
    mycursor.execute(sql)
    # mycursor.execute(
    #     )
    # mycursor.execute("CREATE TABLE customers")
    print("Table is created")


def insert_data(conn,data):
    now = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    mycursor = conn.cursor()
    sql = """INSERT INTO DATA
        (time,nodeId,firmware,battery_percent, 
        counter, source_address, rms_x, rms_y,
         rms_z, max_x, max_y, max_z,
          min_x, min_y, min_z, temperature)
         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    value=(data[0],data[1],data[2],data[4],
           data[5],data[7],data[9],data[10],
           data[11],data[12],data[13],data[14],
           data[15],data[16],data[17],data[18])
    try:
        mycursor.execute(sql,value)
        conn.commit()
        print("inserted "+now)
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)


# conn = connect_database()
# create_table(conn)
# insert_data(conn)
