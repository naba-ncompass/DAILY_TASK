
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
        print("Connection Open")
        return cnx


def create_single_record(sql_connector,cursor):
    try:
        sql_command = "INSERT into students (id,name,dept) values (%s,%s,%s)"
        val =(4,"Naba","IT")
        cursor.execute(sql_command,val)

    except Error as err:
        print(err)
        exit(1)

    except Exception as e:
        print(e)
        exit(1)

    else:
        sql_connector.commit()
        print(cursor.rowcount, "record inserted")
    

def read_all_records(cursor):
    try:
        sql_command = "SELECT * FROM students"
        cursor.execute(sql_command)
        results = cursor.fetchall()

    except Error as err:
        print(err)
        exit(1)

    except Exception as e:
        print(e)
        exit(1)

    else:
        for record in results:
            print(record)


def read_specific_record(cursor):
    try:
        sql_command = "SELECT * FROM students WHERE ID = %s"
        val= (2,)
        cursor.execute(sql_command,val)
        record = cursor.fetchone()

    except Error as err:
        print(err)
        exit(1)

    except Exception as e:
        print(e)
        exit(1)

    else:
        print(record)


def update_record(sql_connector,cursor):
    try:
        sql_command = "UPDATE students SET NAME = %s WHERE ID = %s"
        val = ("Ashish",2)
        cursor.execute(sql_command,val)
        
    except Error as err:
        print(err)
        exit(1)

    except Exception as e:
        print(e)
        exit(1)

    else:
        sql_connector.commit()
        print(cursor.rowcount, "record/s updated")

def delete_record(sql_connector,cursor):
    try:
        sql_command = "DELETE FROM students WHERE ID = %s"
        val = (4,)
        cursor.execute(sql_command,val)
        
    except Error as err:
        print(err)
        exit(1)

    except Exception as e:
        print(e)
        exit(1)

    else:
        sql_connector.commit()
        print(cursor.rowcount, "record/s deleted")


def dml(choice):
    match choice:
        case 1:
            create_single_record(sql_connector,sql_cursor)

        case 2:
            read_all_records(sql_cursor)
        
        case 3:
            read_specific_record(sql_cursor)

        case 4:
            update_record(sql_connector,sql_cursor)

        case 5:
            delete_record(sql_connector,sql_cursor)
    


sql_connector  = create_connection()
sql_cursor = sql_connector.cursor()

choice = -1
while(choice!=6):
    print("\nEnter \n1.CREATE record\n2.READ records\n3.READ specific record\n4.UPDATE record\n5.DELETE record\n6.Exit")
    choice = int(input())
    dml(choice)

sql_connector.close()
print("Connection Closed")

