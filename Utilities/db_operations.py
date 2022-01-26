import pymysql
import json
import time
from .error_handler import *
with open('Config/config.json') as f:
    config = json.load(f)
    db_config = config["DB_CONFIG"]

def create_connection():
    try:
        db = pymysql.connect(host=db_config["DB_HOST"],
                             user=db_config["DB_USER"],
                             password=db_config["DB_PASS"],
                             database=db_config["DB"],
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        return db
    except Exception as e:
        return generate_response(e)


def insert_row(query):
    try:
        start = time.time()
        db = create_connection()
        cursor = db.cursor()
        cursor.execute(query)
    except Exception as e:
        return generate_response(e)

    else:
        rc = cursor.rowcount
        db.commit()
        db.close()
        end = time.time()
        return {'data': rc, "start_time": start, "end_time": end}


def update_row(query):
    try:
        start = time.time()
        db = create_connection()
        cursor = db.cursor()
        cursor.execute(query)
        rc = cursor.rowcount
        db.commit()
        db.close()
        end = time.time()
        return {"data": rc, "start_time": start, "end_time": end}
    except Exception as e:
        return generate_response(e)


def delete_row(query):
    try:
        start = time.time()
        db = create_connection()
        cursor = db.cursor()
        cursor.execute(query)
        rc = cursor.rowcount
        db.commit()
        db.close()
        end = time.time()
        return {"data": rc, "start_time": start, "end_time": end}
    except Exception as e:
        return generate_response(e)


def read_row(query):
    start = time.time()
    db = create_connection()
    cursor = db.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    db.close()
    end = time.time()

    return {"data": data, "start_time": start, "end_time": end}


# ------------ DEVICE DB OPERATIONS ----------

def device_operation(query):
    try:
        start = time.time()
        db = create_connection()
        cursor = db.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        db.commit()
        db.close()
        end = time.time()
        return {"data": data, "start_time": start, "end_time": end}
    except Exception as e:
        return generate_response(e)

