from ast import excepthandler
from multiprocessing.sharedctypes import Value
from os import truncate
import mysql.connector
import json 
from Utilities import error_handler 

def connect():
    try:
        with open("Config/config.json") as f:
            config = json.load(f)

        conn = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database= config["database"]
        )
        # print("sucessfully connected to DATABASE")
    except Exception as e:
        return error_handler.generate_error_response(e)    
    return conn




# def create(query):
#     conn = connect()
#     cursor = conn.cursor()
#     #  work is pending 
#     # query = '''
#     # INSERT INTO employee (id, first_name, last_name, email, gender, phone) VALUES (%s, %s, %s, %s, %s, %s);
#     # '''
#     try:
#             # data = [
#             #     (1, 'NABA', 'Cron', 'mcronchey0@pen.io', 'F', '314-289-7265'),
#             #     (2, 'ASHISH', 'Mus', 'tmushrow1@whitehouse.gov', 'F', '804-163-9834'),
#             #     (3, 'ARJIEET', 'Boll', 'mbonicelli2@sitemeter.com', 'F', '624-922-2416'),
#             #     (4, 'MEGHNA', 'Wat', 'lwatkinson3@accuweather.com', 'M', '456-260-1052'),
#             #     (5, 'prem', 'raj', 'bwilcot4@twitpic.com', 'M', '608-344-4090')
#             # ]
#             cursor.executemany(query)
#             records = cursor.rowcount
#             # print('{} records inserted'.format(cursor.rowcount))
#             # print('-------------------------------------')
#             # naba()
#     except Exception as e:
#         print("ERROR MESSAGE:",e) 
#     else:
#         conn.commit()   
#         conn.close() 
#         return records   


def insert(query):
    conn = connect()
    cursor = conn.cursor()
    # query = "INSERT INTO employee (id, first_name, last_name, email, gender, phone) VALUES (%s, %s, %s, %s, %s, %s);"
    try:
        cursor.execute(query)
        # records = cursor.rowcount
        # id = input["id"]
        # first_name= input["first_name"]
        # last_name= input["last_name"]
        # email= input["email"]
        # gender= input["gender"]
        # phone = input["phone"]
        # data= (id, first_name,last_name,email,gender,phone)
        # print('-------------------------------------')
        # naba()
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
            # records = cursor.rowcount
            # input_name = input["first_name"]
            # input_id = input["id"]
            # conn.commit()
            # records = cursor.fetchall()
            # print('Employee id = {} updated successfully'.format(input_id))
            # print('-------------------------------------')
            # naba()

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
    # query = '''DELETE FROM employee WHERE id = %s;'''
    try:
            # input_id = input["id"]    
            cursor.execute(query)
            # records = cursor.rowcount
            # conn.commit()
            # records = cursor.fetchall()
            # print('Employee id = {} deleted successfully'.format(input_id))
            # print("THIS FUNCTION WILL ONLY DELETE SPECIFIC ID")
            # print('-------------------------------------')
            # naba() 
    except Exception as e:
        return error_handler.generate_error_response(e) 
    else:
        msg = str(cursor.rowcount) + ' record deleted'
        conn.commit()   
        conn.close() 
        return msg     


def get_all(query):
    conn = connect()
    cursor = conn.cursor()
    # query = "SELECT * FROM employee;"
    try:
            cursor.execute(query)
            # records = cursor.fetchall()
            # print('EMPLOYEE INFORMATION')
            # print('-------------------------------------')
            # for i in records:
            #     print(i)
            # naba()
    except Exception as e:
        return error_handler.generate_error_response(e)
        # print("ERROR MESSAGE:",e) 
    else:
        msg = cursor.fetchall()
        conn.commit()   
        conn.close() 
        return msg   

def truncate(query):
    conn = connect()
    cursor = conn.cursor()
    # query = "truncate table employee;"
    try:
        cursor.execute(query)
        records = cursor.rowcount
        # print('TRUNCATE will empty the table')
        # print('-------------------------------------------')
        # naba()
    except Exception as e:
        return error_handler.generate_error_response(e)  
    else:
        # msg = str(cursor.rowcount) + ' truncate deleted'
        conn.commit()   
        conn.close() 
        return records       
