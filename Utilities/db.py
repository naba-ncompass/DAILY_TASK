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


def create(sql_query):
    sql_connector = create_connection()
    cursor = sql_connector.cursor()
    cursor.execute(sql_query)

    sql_connector.commit()
    row_count = cursor.rowcount
    close_connection(sql_connector)
    return row_count
    

def read_all(sql_query):
    sql_connector = create_connection()
    cursor = sql_connector.cursor()
    cursor.execute(sql_query)

    results = cursor.fetchall()
    close_connection(sql_connector)
    return results


def read_specific(sql_query):
    sql_connector = create_connection()
    cursor = sql_connector.cursor()
    cursor.execute(sql_query)

    record = cursor.fetchone()
    close_connection(sql_connector)
    return record


def update(sql_query):
    sql_connector = create_connection()
    cursor = sql_connector.cursor()
    cursor.execute(sql_query)
    
    sql_connector.commit()
    row_count = cursor.rowcount
    close_connection(sql_connector)
    return row_count

def delete(sql_query):
    sql_connector = create_connection()
    cursor = sql_connector.cursor()
    cursor.execute(sql_query)

    sql_connector.commit()
    row_count = cursor.rowcount
    close_connection(sql_connector)
    return row_count

def check_record(sql_query):
    sql_connector = create_connection()
    cursor = sql_connector.cursor()
    cursor.execute(sql_query)

    result = cursor.fetchone()
    close_connection(sql_connector)
    return result

# ------------- DEVICE  USECASE -----------------------#

def create_connection_device():
    with open("Config/config.json") as f:
        config = json.load(f)
    cnx2 = connection.MySQLConnection(**config["device"])
    return cnx2


def close_connection_device(sql_connector):
    sql_connector.close()


def read_peak_consumption(sql_query):
    sql_connector1 = create_connection_device()
    cursor = sql_connector1.cursor()
    cursor.execute(sql_query)

    record = cursor.fetchone()
    close_connection_device(sql_connector1)
    return record

def read_sum_consumption(sql_query):
    sql_connector1 = create_connection_device()
    cursor = sql_connector1.cursor()
    cursor.execute(sql_query)

    record = cursor.fetchone()
    close_connection_device(sql_connector1)
    return record

def read_duplicate_time(sql_query):
    sql_connector1 = create_connection_device()
    cursor = sql_connector1.cursor()
    cursor.execute(sql_query)

    record = cursor.fetchall()
    close_connection_device(sql_connector1)
    return record







