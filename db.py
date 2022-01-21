
from mysql.connector import (connection,errorcode,Error)


def create_connection():
    try:
        config = {
            'user':'pythonMysql',
            'password':'pythonMysql',
            'host':'127.0.0.1',
            'database':'newdatabase'
        }

        cnx = connection.MySQLConnection(**config) 

    except Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            exit(1)
        else:
            print(err)
    
    else:
        return cnx


def close_connection(sql_connector):
    try:
        sql_connector.close()

    except Error as err:
        print(err)
        exit(1)

    
def table_schema():
    print("Table Schema:")
    try:
        sql_connector = create_connection()
        cursor = sql_connector.cursor()

        sql_command = "DESC students"
        cursor.execute(sql_command)

    except Error as err:
        print(err)
        exit(1)

    except Exception as e:
        print(e)
        exit(1)

    else:
        schema = cursor.fetchall()
        close_connection(sql_connector)
        return schema
        
       
def create_single_record(record):
    try:
        sql_connector = create_connection()
        cursor = sql_connector.cursor()

        _id = record['id']
        name = record['name']
        dept = record['dept']

        sql_command = "INSERT into students (id,name,dept) values (%s,%s,%s)"
        val= (_id,name,dept)

        cursor.execute(sql_command,val)

    except Error as err:
        print(err)
        exit(1)

    except Exception as e:
        print(e)
        exit(1)

    else:
        sql_connector.commit()
        row_count = cursor.rowcount
        close_connection(sql_connector)
        return row_count
    

def read_all_records():
    try:
        sql_connector = create_connection()
        cursor = sql_connector.cursor()

        sql_command = "SELECT * FROM students"
        cursor.execute(sql_command)

    except Error as err:
        print(err)
        exit(1)

    except Exception as e:
        print(e)
        exit(1)

    else:
        results = cursor.fetchall()
        close_connection(sql_connector)
        return results


def read_specific_record(id):
    try:
        sql_connector = create_connection()
        cursor = sql_connector.cursor()

        sql_command = "SELECT * FROM students WHERE ID = %s"
        val = (id,)
        cursor.execute(sql_command,val)
       

    except Error as err:
        print(err)
        exit(1)

    except Exception as e:
        print(e)
        exit(1)

    else:
        record = cursor.fetchone()
        close_connection(sql_connector)
        return record


def update_record(info):
    try:
        sql_connector = create_connection()
        cursor = sql_connector.cursor()

        _id = info['id']
        column_name = info['column_name']
        value = info['value']

        sql_command = f"UPDATE students SET {column_name} = %s WHERE ID = %s"
        val = (value,_id)
        cursor.execute(sql_command,val)
        
    except Error as err:
        print(err)
        exit(1)

    except Exception as e:
        print(e)
        exit(1)

    else:
        sql_connector.commit()
        row_count = cursor.rowcount
        close_connection(sql_connector)
        return row_count

def delete_record(id):
    try:
        sql_connector = create_connection()
        cursor = sql_connector.cursor()

        sql_command = "DELETE FROM students WHERE ID = %s"
        val = (id,)
        cursor.execute(sql_command,val)
        
    except Error as err:
        print(err)
        exit(1)

    except Exception as e:
        print(e)
        exit(1)

    else:
        sql_connector.commit()
        row_count = cursor.rowcount
        close_connection(sql_connector)
        return row_count

