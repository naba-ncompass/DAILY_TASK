from multiprocessing.sharedctypes import Value
from os import truncate
import mysql.connector

def connect():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user="root",
            password="Naba@2001",
            database= "demo"
        )
        print("sucessfully connected to DATABASE")
    except Exception as e:
        print("ERROR MESSAGE:",e)    
    return conn


def naba():
    print('Available Options:\n C=INSERT \n R=Read \n U=Update \n D=Delete \n T= TRUNCATE \n X= CLOSE ')
    choice = input('Choose your option = ')
    conn = connect()
    try:
        if choice == 'C':
            # data = input("INSERT NAME EVERYTHING:")
            create(conn)
        elif choice == 'I':
            id = input('Enter id of Student: ')
            first_name = input('Enter FRIST name of Student: ')
            last_name = input('Enter LASTname of Student: ')
            email = input('ENTER email id:')
            gender = input('ENTER gender: ')
            phone = input('Enter Phone Number: ')
            insert(conn,id,first_name,last_name,email,gender,phone)      
        elif choice == 'R':
            get_all()   
        elif choice == 'U':
            input_id = input("WHICH ID YOU WANT TO UPDATE: ")
            input_name = input("WHAT NAME WOULD YOU LIKE TO UPDATE: ")
            update(conn, input_name,input_id)
        elif choice == 'D':
            input_id = input("WHICH ID YOU WANT TO DELETE: ")
            delete(conn, input_id)
        elif choice == 'T':
            truncate(conn)
        elif choice == 'X':
            conn.close()
        else:
            print('Wrong choice, You are going exist.')
            conn.close()
    except Exception as e:
        print("NOTHING MUCH RESTART THE PROGRAM ")


def create(conn):
    cursor = conn.cursor()
    #  work is pending 
    query = '''
    INSERT INTO employee (id, first_name, last_name, email, gender, phone) VALUES (%s, %s, %s, %s, %s, %s);
    '''
    try:
            data = [
                (1, 'NABA', 'Cron', 'mcronchey0@pen.io', 'F', '314-289-7265'),
                (2, 'ASHISH', 'Mus', 'tmushrow1@whitehouse.gov', 'F', '804-163-9834'),
                (3, 'ARJIEET', 'Boll', 'mbonicelli2@sitemeter.com', 'F', '624-922-2416'),
                (4, 'MEGHNA', 'Wat', 'lwatkinson3@accuweather.com', 'M', '456-260-1052'),
                (5, 'prem', 'raj', 'bwilcot4@twitpic.com', 'M', '608-344-4090')
            ]
            cursor.executemany(query, data)
            conn.commit()
            print('{} records inserted'.format(cursor.rowcount))
            print('-------------------------------------')
            naba()
    except Exception as e:
        print("ERROR MESSAGE:",e)    


def insert(conn,id,first_name,last_name,email,gender,phone):
    cursor = conn.cursor()
    query = "INSERT INTO employee (id, first_name, last_name, email, gender, phone) VALUES (%s, %s, %s, %s, %s, %s);"
    try:
        data= (id, first_name,last_name,email,gender,phone)
        cursor.execute(query, data)
        conn.commit()    
        print('-------------------------------------')
        naba()
    except Exception as e:
        print("ERROR MESSAGE:",e)   

def update(conn, input_name,input_id):
    cursor = conn.cursor()
    query = '''UPDATE employee SET first_name = %s WHERE id = %s;'''
    try:
            cursor.execute(query, [input_name,input_id ])
            conn.commit()
            print('Employee id = {} updated successfully'.format(input_id))
            print('-------------------------------------')
            naba()

    except Exception as e:
        print("ERROR MESSAGE:",e)    


def delete(conn, input_id):
    cursor = conn.cursor()
    query = '''DELETE FROM employee WHERE id = %s;'''
    try:
            cursor.execute(query, [input_id])
            conn.commit()
            print('Employee id = {} deleted successfully'.format(input_id))
            print("THIS FUNCTION WILL ONLY DELETE SPECIFIC ID")
            print('-------------------------------------')
            naba()
    except Exception as e:
        print("ERROR MESSAGE:",e)    


def get_all():
    conn = connect()
    cursor = conn.cursor()
    query = "SELECT * FROM employee;"
    try:
            cursor.execute(query)
            records = cursor.fetchall()
            # print('EMPLOYEE INFORMATION')
            # print('-------------------------------------')
            # for i in records:
            #     print(i)
            # naba()
    except Exception as e:
        print("ERROR MESSAGE:",e) 
    else:
        return records   

def truncate(conn):
    cursor = conn.cursor()
    query = "truncate table employee;"
    try:
        cursor.execute(query)
        print('TRUNCATE will empty the table')
        print('-------------------------------------------')
        naba()
    except Exception as e:
        print("ERROR MESSAGE:",e)    

