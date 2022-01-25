import mysql.connector as sql
from Utilities import error_handler
import json

with open('config/config.json','r') as c:
    db_credentials = json.load(c)["db_credentials"]

def connection():
    
    try:
        mydb = sql.connect(
            host = db_credentials['host'],
            user = db_credentials['user'],
            password = db_credentials['password'],
            database = db_credentials['database']
        )
        return mydb
    except Exception as e:
        return error_handler.generate_error_response('connection error')
        



def insert_into_table(query):
    
    try:
        mydb = connection()
        dbcursor = mydb.cursor()
        dbcursor.execute(query)
        message = str(dbcursor.rowcount) + ' record inserted'
        mydb.commit()
        mydb.close()
        return message
    except Exception as e:
        return error_handler.generate_error_response(e.msg)
        



def read_from_table(query):

    try:
        mydb = connection()
        dbcursor = mydb.cursor()
        dbcursor.execute(query)
        output = dbcursor.fetchall()
        mydb.close()
        return output
    except Exception as e:
        return error_handler.generate_error_response(e.msg)
        
    
    
    



def update_table(query):
   
    try:
        mydb = connection()
        dbcursor = mydb.cursor()
        dbcursor.execute(query)
        message = str(dbcursor.rowcount) + ' record updated'
        mydb.commit()
        mydb.close()
        return message
    except Exception as e:
        return error_handler.generate_error_response(e.msg)
        



def delete_from_table(query):
    
    try:
        mydb = connection()
        dbcursor = mydb.cursor()
        dbcursor.execute(query)
        message = str(dbcursor.rowcount) + ' record deleted'
        mydb.commit()
        mydb.close()
        return message
    except Exception as e:
        return error_handler.generate_error_response(e.msg)