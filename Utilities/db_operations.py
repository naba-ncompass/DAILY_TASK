
#!/usr/bin/python3
import pymysql
import json


with open('Config/config.json') as f:
    config = json.load(f)


def create_connection():
    try:
        db = pymysql.connect(host='localhost',
                             user=config["DB_USER"],
                             password=config["DB_PASS"],
                             database='Practice',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        return db
    except Exception as e:
        return {"ERROR" : e}


def insert_row(query):
    try:
        db = create_connection()
        cursor = db.cursor()
        cursor.execute(query)
        rc = cursor.rowcount
        db.commit()
        db.close()
        return {"rowcount" : rc , "message" : "row inserted successfully"}
    except Exception as e:
        return {"ERROR" : e}


def update_row(query):
    try:
        db = create_connection()
        cursor = db.cursor()
        cursor.execute(query)
        rc = cursor.rowcount
        db.commit()
        db.close()
        return {"rowcount" : rc , "message" : "row updated successfully"}
    except Exception as e:
        return {"ERROR" : e}


def delete_row(query):
    try:
        db = create_connection()
        cursor = db.cursor()
        cursor.execute(query)
        rc = cursor.rowcount
        db.commit()
        db.close()
        return {"rowcount" : rc , "message" : "row deleted successfully"}
    except Exception as e:
        return {"ERROR" : e}


def read_row(query):
    db = create_connection()
    cursor= db.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    db.close()
    if len(data) == 0:
        return {"message" : "Table is Empty"}

    return data


