import mysql.connector as sql

def connection():
    
    try:
        mydb = sql.connect(
            host='localhost',
            user='ash3',
            password='ash3',
            database='experiments'
        )
    except Exception as e:
        print(e)
        print("Couldn't connect to database!! Something went wrong...")
    else:
        print("\n Connection to database successfull !! \n")
    return mydb



def insert_into_student(data):
    
    try:
        mydb = connection()
    except Exception as e:
        print(e)
        print("Connection Failed !!!")
    else:
        dbcursor = mydb.cursor()
        try:
            query = "insert into student values (%s, %s, %s, %s)"
            values = (data['id'], data['name'], data['department'], data['cgpa'])
            dbcursor.execute(,data)
        except Exception as e:
            print(e)
        else:
            print(dbcursor.rowcount,'record inserted')
            mydb.commit()
            mydb.close()



def read_from_student():

    try:
        mydb = connection()
    except Exception as e:
        print(e)
        print("Connection Failed !!!")
    else:
        dbcursor = mydb.cursor()
        try:
            dbcursor.execute("select * from student")
        except Exception as e:
            print(e)
        else:
            output = dbcursor.fetchall()
            for i in output:
                print(i)
            print('\n',dbcursor.rowcount,'records fetched')
            mydb.close()
    return output
    
    



def update_student(data):
   
    try:
        mydb = connection()
    except Exception as e:
        print(e)
        print("Connection Failed !!!")
    else:
        dbcursor = mydb.cursor()
        try:
            query = "update student set " + data[0] +" = %s where "+ data[2] +" = %s"
            input_var = (data[1], data[3])
            dbcursor.execute(query, input_var)
        except Exception as e:
            print(e)
            print('operation failed !!! Something went wrong...')
        else:
            print(dbcursor.rowcount,'record updated')
            mydb.commit()
            mydb.close()



def delete_from_student(data):
    
    try:
        mydb = connection()
    except Exception as e:
        print(e)
        print("Connection Failed !!!")
    else:
        dbcursor = mydb.cursor()
        try:
            query = "delete from student where +" + data[0] + " = %s"
            input_var = (data[1],)
            dbcursor.execute(query, input_var)
        except Exception as e:
            print(e)
            print('operation failed !!! Something went wrong...')
        else:
            print(dbcursor.rowcount,'record deleted')
            mydb.commit()
            mydb.close()
