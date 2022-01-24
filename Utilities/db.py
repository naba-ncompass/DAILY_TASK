from mysql.connector import connection
import json

#-----------------STUDENTS USECASE --------------------#

def create_connection():
    with open("Config/config.json") as f:
        config = json.load(f)
    cnx = connection.MySQLConnection(**config["students"])
    return cnx


def close_connection(sql_connector):
    sql_connector.close()


def create_single_record(sql_command):
    sql_connector = create_connection()
    cursor = sql_connector.cursor()
    cursor.execute(sql_command)

    sql_connector.commit()
    row_count = cursor.rowcount
    close_connection(sql_connector)
    return row_count
    

def read_all_records(sql_command):
    sql_connector = create_connection()
    cursor = sql_connector.cursor()
    cursor.execute(sql_command)

    results = cursor.fetchall()
    close_connection(sql_connector)
    return results


def read_specific_record(sql_command):
    sql_connector = create_connection()
    cursor = sql_connector.cursor()
    cursor.execute(sql_command)

    record = cursor.fetchone()
    close_connection(sql_connector)
    return record


def update_record(sql_command):
    sql_connector = create_connection()
    cursor = sql_connector.cursor()
    cursor.execute(sql_command)
    
    sql_connector.commit()
    row_count = cursor.rowcount
    close_connection(sql_connector)
    return row_count

def delete_record(sql_command):
    sql_connector = create_connection()
    cursor = sql_connector.cursor()
    cursor.execute(sql_command)

    sql_connector.commit()
    row_count = cursor.rowcount
    close_connection(sql_connector)
    return row_count

# ------------- DEVICE  USECASE -----------------------#

def create_connection_device():
    with open("Config/config.json") as f:
        config = json.load(f)
    cnx2 = connection.MySQLConnection(**config["device"])
    return cnx2


def close_connection_device(sql_connector):
    sql_connector.close()


def read_peak_consumption_between_times(sql_command):
    sql_connector1 = create_connection_device()
    cursor = sql_connector1.cursor()
    cursor.execute(sql_command)

    record = cursor.fetchone()
    close_connection_device(sql_connector1)
    return record

def read_sum_consumption_between_times(sql_command):
    sql_connector1 = create_connection_device()
    cursor = sql_connector1.cursor()
    cursor.execute(sql_command)

    record = cursor.fetchone()
    close_connection_device(sql_connector1)
    return record

def read_duplicate_time_between_times(sql_command):
    sql_connector1 = create_connection_device()
    cursor = sql_connector1.cursor()
    cursor.execute(sql_command)

    record = cursor.fetchall()
    close_connection_device(sql_connector1)
    return record







