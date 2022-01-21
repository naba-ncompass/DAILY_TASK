
#!/usr/bin/python3
from venv import create
import pymysql

def create_connection():
    try:
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='princess',
                             database='Practice',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        return db
    except Exception as e:
        return {"ERROR" : e}


def insert_row(data):
    try:
        db = create_connection()
        cursor = db.cursor()
        cursor.execute('INSERT INTO TvShows VALUES (%d , "%s" , "%s" );'%(
            data['id'], data['name'], data['studio']))
        rc = cursor.rowcount
        db.commit()
        db.close()
        return {"rowcount" : rc , "message" : "row inserted successfully"}
    except Exception as e:
        return {"ERROR" : e}


def update_row(data):
    try:
        db = create_connection()
        cursor = db.cursor()
        cursor.execute('UPDATE TvShows SET %s="%s" WHERE id = %d;'%(
            data['column'], data['new_value'], data['id']))
        rc = cursor.rowcount
        db.commit()
        db.close()
        return {"rowcount" : rc , "message" : "row updated successfully"}
    except Exception as e:
        return {"ERROR" : e}


def delete_row(data):
    try:
        db = create_connection()
        cursor = db.cursor()
        cursor.execute('DELETE FROM TvShows WHERE id = %d ;'%(data['id']))
        rc = cursor.rowcount
        db.commit()
        db.close()
        return {"rowcount" : rc , "message" : "row deleted successfully"}
    except Exception as e:
        return {"ERROR" : e}


def read_row():
    db = create_connection()
    cursor= db.cursor()
    cursor.execute('SELECT * FROM TvShows')
    data = cursor.fetchall()
    db.close()
    if len(data) == 0:
        return {"message" : "Table is Empty"}

    return data


