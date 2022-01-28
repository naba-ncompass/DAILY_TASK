import mysql.connector
import json 
from Utilities import error_handler 
from timeit import default_timer as timer
from datetime import datetime,timedelta

def give_response(data,message,start_time):
    end_time = datetime.now()
    duration = end_time - start_time
    response = {
        "start_time": start_time.strftime("%H:%M:%S.%f"),
        "success": True,
        "data": data,
        "message":message,
        "end_time": end_time.strftime("%H:%M:%S.%f"),
        "duration":duration.total_seconds()
    }
    return response

def connect():
    try:
        with open("Config/config.json",'r') as r:
            config = json.load(r)
        conn = mysql.connector.connect(
            host=config['host'],
            user=config['user'],
            password=config['password'],
            database= config['database'],
            auth_plugin='mysql_native_password'
        )
        return conn
    except Exception as e:
        return (e)
        # return error_handler.generate_error_response(e)    

        



def insert(query):
    conn = connect()
    cursor = conn.cursor()
    # query = "INSERT INTO employee (id, first_name, last_name, email, gender, phone) VALUES (%s, %s, %s, %s, %s, %s);"
    try:
        cursor.execute(query)
    except Exception as e:
        return error_handler.generate_error_response(e)  
    else:
        msg = str(cursor.rowcount) + ' record inserted'
        conn.commit()   
        conn.close() 
        return msg 

def update(query):
    conn = connect()
    cursor = conn.cursor()
    # query = '''UPDATE employee SET first_name = %s WHERE id = %s;'''
    try:
            cursor.execute(query)
    except Exception as e:
        return error_handler.generate_error_response(e)    

    else:
        msg = str(cursor.rowcount) + ' record updated'
        conn.commit()   
        conn.close() 
        return msg

def delete(query):
    conn = connect()
    cursor = conn.cursor()
    try:
            cursor.execute(query)
    except Exception as e:
        return error_handler.generate_error_response(e) 
    else:
        msg = str(cursor.rowcount) + ' record deleted'
        conn.commit()   
        conn.close() 
        return msg     


def get_all(query):
    try:
            conn = connect()
            print(conn)
            cursor = conn.cursor()
            cursor.execute(query)
            msg = cursor.fetchall()
            conn.commit()
            conn.close() 
            return msg
    except Exception as e:
        return error_handler.generate_error_response(e) 


def get_all_id(query):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
    except Exception as e:
        return error_handler.generate_error_response(e) 
    else:
        msg = cursor.fetchall()
        conn.commit()   
        conn.close() 
        return msg 


def truncate(query):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        records = cursor.rowcount
    except Exception as e:
        return error_handler.generate_error_response(e)  
    else:
        conn.commit()   
        conn.close() 
        return records       

#  -------------------DEVICE CASE---------------------

def read(query):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
    except Exception as e:
        return error_handler.generate_error_response(e) 
    else:
        msg = cursor.fetchall()
        conn.commit()   
        conn.close() 
        return msg 