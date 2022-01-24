from urllib import response
from Utilities.db import *
from flask import Flask,jsonify,request,Blueprint
from timeit import default_timer as timer
from datetime import datetime,timedelta
from Utilities import db

def show_item():
        start_time = datetime.now()
        query = "select * from employee;"
        var = db.get_all(query)
        return jsonify(give_response(data=var, message='operation successful', start_time=start_time))


def insert_operation():
    start_time = datetime.now()
    input = {}
    input = request.get_json()
    query = "INSERT INTO employee (id, first_name, last_name, email, gender, phone) VALUES (%s, '%s', '%s', '%s', '%s', '%s');"%(input["id"],input["first_name"],input["last_name"],input["email"],input["gender"],input["phone"])
    message = db.insert(query)
    return jsonify(give_response(data=[], message=message, start_time=start_time))  

def update_operation():
    start_time = datetime.now()
    input = {}
    input = request.get_json()
    query = "UPDATE employee SET first_name = '%s' WHERE id = %s;"%(input["first_name"],input["id"])
    message = db.update(query)
    return jsonify(give_response(data=[], message=message, start_time=start_time))

def delete_operation():
    start_time = datetime.now()
    input = {}
    input = request.get_json()
    query = "DELETE FROM employee WHERE id = %s;"%(input["id"])
    message = db.delete(query)
    return jsonify(give_response(data=[], message=message, start_time=start_time))

# def create_operation():
#     input = {}
#     input = request.get_json()
#     query = "INSERT INTO employee (id, first_name, last_name, email, gender, phone) VALUES (%s, '%s', '%s', '%s', '%s', '%s');"%(input["id"],input["first_name"],input["last_name"],input["email"],input["gender"],input["phone"])
#     response = db.insert(query)
#     return jsonify(response)

def truncate_operation():
    start_time = datetime.now()
    query = "truncate table employee;"
    message = db.truncate(query)
    return jsonify(give_response(data=[], message=message, start_time=start_time))
    # response = db.insert(query)
    # return jsonify(response)

# def generate_response():
#     return jsonify(response)


def give_response(data,message,start_time):
    end_time = datetime.now()
    duration = end_time - start_time
    response = {
        "start_time": start_time.strftime("%H:%M:%S.%f"),
        "success": True,
        "data": data,
        "message":message,
        "end_time": end_time.strftime("%H:%M:%S.%f"),
        "duration":duration.total_seconds()
    }
    return response