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
        return e
    else:
        return mydb



def insert_into_student(data):
    
    try:
        mydb = connection()
    except Exception as e:
        return e
    else:
        dbcursor = mydb.cursor()
        try:
            query = "insert into student values (%s, %s, %s, %s)"
            values = (data['id'], data['name'], data['department'], data['cgpa'])
            dbcursor.execute(query, values)
        except Exception as e:
            return e
        else:
            msg = str(dbcursor.rowcount) + ' record inserted'
            mydb.commit()
            mydb.close()
            return msg



def read_from_student():

    try:
        mydb = connection()
    except Exception as e:
        return e
    else:
        dbcursor = mydb.cursor()
        try:
            dbcursor.execute("select * from student")
        except Exception as e:
            return e
        else:
            output = dbcursor.fetchall()
            mydb.close()
    return output
    
    



def update_student(data):
   
    try:
        mydb = connection()
    except Exception as e:
        return e
    else:
        dbcursor = mydb.cursor()
        try:
            query = "update student set " + data["change_col"] + " = %s where "+ data["where_col"] +" = %s"
            input_var = (data["new_value"], data["where_value"])
            dbcursor.execute(query, input_var)
        except Exception as e:
            return e
        else:
            msg = str(dbcursor.rowcount) + ' record updated'
            mydb.commit()
            mydb.close()
            return msg



def delete_from_student(data):
    
    try:
        mydb = connection()
    except Exception as e:
        return e
    else:
        dbcursor = mydb.cursor()
        try:
            query = "delete from student where +" + data["where_col"] + " = %s"
            input_var = (data["where_value"],)
            dbcursor.execute(query, input_var)
        except Exception as e:
            return e
        else:
            msg = str(dbcursor.rowcount) + ' record deleted'
            mydb.commit()
            mydb.close()
            return msg
