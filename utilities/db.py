import mysql.connector as sql
import json
from Utilities import error_handler

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
    except Exception as e:
        return error_handler.generate_error_response(e)
    else:
        return mydb



def insert_into_student(query):
    
    try:
        mydb = connection()
    except Exception as e:
        return error_handler.generate_error_response(e)
    else:
        dbcursor = mydb.cursor()
        try:
            dbcursor.execute(query)
        except Exception as e:
            return error_handler.generate_error_response(e)
        else:
            msg = str(dbcursor.rowcount) + ' record inserted'
            mydb.commit()
            mydb.close()
            return msg



def read_from_student(query):

    try:
        mydb = connection()
    except Exception as e:
        return error_handler.generate_error_response(e)
    else:
        dbcursor = mydb.cursor()
        try:
            dbcursor.execute(query)
        except Exception as e:
            return error_handler.generate_error_response(e)
        else:
            output = dbcursor.fetchall()
            mydb.close()
    return output
    
    



def update_student(query):
   
    try:
        mydb = connection()
    except Exception as e:
        return error_handler.generate_error_response(e)
    else:
        dbcursor = mydb.cursor()
        try:
            dbcursor.execute(query)
        except Exception as e:
            return error_handler.generate_error_response(e)
        else:
            msg = str(dbcursor.rowcount) + ' record updated'
            mydb.commit()
            mydb.close()
            return msg



def delete_from_student(query):
    
    try:
        mydb = connection()
    except Exception as e:
        return error_handler.generate_error_response(e)
    else:
        dbcursor = mydb.cursor()
        try:
            dbcursor.execute(query)
        except Exception as e:
            return error_handler.generate_error_response(e)
        else:
            msg = str(dbcursor.rowcount) + ' record deleted'
            mydb.commit()
            mydb.close()
            return msg
