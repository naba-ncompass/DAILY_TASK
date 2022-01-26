from urllib import response
from wsgiref.validate import validator
from Employee.validation import validation_check, validation_insert, validation_insert_id, validation_update
from Utilities.db import *
from flask import Flask,jsonify,request,Blueprint
from timeit import default_timer as timer
from datetime import datetime,timedelta
from Utilities import db
import hashlib


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


def give_hash(input):
    hash = hashlib.md5(input.encode())
    return hash.hexdigest()

def read_employee():
        start_time = datetime.now()
        query = "select * from employee;"
        var = db.get_all(query)
        return jsonify(give_response(data=var, message='operation successful', start_time=start_time))

def read_employee_id():
    start_time = datetime.now()
    value = request.args
    v= validation_insert_id(value)
    if isinstance(v,bool):
        query = "select * from employee where id = %s;"%(int(value["id"]))
        var = db.get_all_id(query)
        return jsonify(give_response(data=var, message='operation successful', start_time=start_time))
    else:
        return jsonify({ "message" : v })
    
  

def insert_employee():
    start_time = datetime.now()
    input = {}
    input = request.get_json()
    v= validation_insert(input)
    if isinstance(v,bool):
        query = "INSERT INTO employee (id, first_name, last_name, email, gender, phone ,password) VALUES (%s, '%s', '%s', '%s', '%s', '%s', '%s');"%(input["id"],input["first_name"],input["last_name"],input["email"],input["gender"],input["phone"],give_hash(input["password"]))
        messages = db.insert(query)
        var = jsonify(give_response(data=messages, message="row is inserted", start_time=start_time))  
        return var 
    else:
        return jsonify({ "message" : v })


def update_employee():
    start_time = datetime.now()
    input = {}
    input = request.get_json()
    v= validation_update(input)
    if isinstance(v,bool):
        query = "UPDATE employee SET first_name = '%s' WHERE id = %s;"%(input["first_name"],input["id"])
        messages = db.update(query)
        return jsonify(give_response(data=messages, message="row is updated", start_time=start_time))
    else:
        return jsonify({ "message" : v })

def delete_employee():
    start_time = datetime.now()
    value = request.args
    v= validation_insert_id(value)
    if isinstance(v,bool):
        query = "DELETE FROM employee WHERE id = %s;"%(int(value["id"]))
        messages = db.delete(query)
        return jsonify(give_response(data=messages, message="Deleted the data", start_time=start_time))
    else:
        return jsonify({ "message" : v })

def truncate_employee():
    start_time = datetime.now()
    query = "truncate table employee;"
    message = db.truncate(query)
    return jsonify(give_response(data=[], message=message, start_time=start_time))

def student_login():
    start_time = datetime.now()
    input = {}
    input = request.get_json()
    v= validation_check(input)
    if isinstance(v,bool):
        query = f"select password from employee where email = '{input['email']}'"
        print("HELLO WORLD")
        message = db.get_all(query)
        if give_hash(input['password']) == message[0][0]:
            return jsonify(give_response(data=[], message="login successful", start_time=start_time))
        else:
            return jsonify(give_response(data=[], message="wrong username or password", start_time=start_time))

    else:
        return jsonify({ "message" : v })

