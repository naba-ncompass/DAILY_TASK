from os import access
from pyexpat.errors import messages
from urllib import response
from wsgiref.validate import validator
from Employee.validation import validation_check, validation_insert, validation_insert_id, validation_update
from Utilities import db
from flask import Flask,jsonify,request,Blueprint
from timeit import default_timer as timer
from datetime import datetime,timedelta
from Utilities import db
import hashlib
from flask_jwt_extended import create_access_token,decode_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


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

def give_response_access_token(data,message,access_token,start_time):
    end_time = datetime.now()
    duration = end_time - start_time
    response = {
        "start_time": start_time.strftime("%H:%M:%S.%f"),
        "success": True,
        "data": data,
        "message":message,
        "end_time": end_time.strftime("%H:%M:%S.%f"),
        "duration":duration.total_seconds(),
        "access_token":access_token
    }
    return response

def test_authorization():
    auth = str(request.headers['Authorization']).split(' ')[1]
    output= decode_token(auth)['sub']
    return output

def give_hash(input):
    hash = hashlib.md5(input.encode())
    return hash.hexdigest()

def check_employee():
    email = test_authorization()
    query = "select email from employee where email = '%s';"%(input[email])
    output = db.read_from_table(query)
    if output[0][0]==1:
        return True
    else:
        return "user not found"


def read_employee():
        start_time = datetime.now()
        query = "select * from employee;"
        var = db.get_all(query)
        return jsonify(give_response(data=var, message='operation successful', start_time=start_time))

def read_employee_id():
        start_time = datetime.now()
        auth = str(request.headers['Authorization']).split(' ')[1]
        output= decode_token(auth)['sub']
        if (output ==1):
            value = request.args
            v= validation_insert_id(value)
            if isinstance(v,bool):
                query = "select * from employee where id = %s;"%(int(value["id"]))
                var = db.get_all_id(query)
                return jsonify(give_response(data=var, message='operation successful', start_time=start_time))
            else:
                return jsonify({ "message" : v })
        else:
            return jsonify(give_response(data=[], message='operation falied', start_time=start_time))


def insert_employee():
    start_time = datetime.now()
    if isinstance(check_employee(),bool):
        input = {}
        input = request.get_json()
        v= validation_insert(input)
        if isinstance(v,bool):
            query = "INSERT INTO employee (id, first_name, last_name, email, gender, phone ,password) VALUES (%s, '%s', '%s', '%s', '%s', '%s', '%s');"%(input["id"],input["first_name"],input["last_name"],input["email"],input["gender"],input["phone"],give_hash(input["password"]))
            messages = db.insert(query)
            var = jsonify(give_response(data=[messages], message="row is inserted", start_time=start_time))  
            return var 
        else:
            return jsonify({ "message" : v })
    else:
         jsonify(give_response(data=[], message="operation failed", start_time=start_time))  


def update_employee():
    start_time = datetime.now()
    if isinstance(check_employee(),bool):
        input = {}
        input = request.get_json()
        v= validation_update(input)
        if isinstance(v,bool):
            query = "UPDATE employee SET first_name = '%s' WHERE id = %s;"%(input["first_name"],input["id"])
            messages = db.update(query)
            return jsonify(give_response(data=messages, message="row is updated", start_time=start_time))
        else:
            return jsonify({ "message" : v })
    else:
        return jsonify(give_response(data=[], message="operation falied", start_time=start_time))


def delete_employee():
    start_time = datetime.now()
    if isinstance(check_employee(),bool):
        value = request.args
        v= validation_insert_id(value)
        if isinstance(v,bool):
            query = "DELETE FROM employee WHERE id = %s;"%(int(value["id"]))
            messages = db.delete(query)
            return jsonify(give_response(data=messages, message="Deleted the data", start_time=start_time))
        else:
            return jsonify({ "message" : v })
    else:
            return jsonify(give_response(data=[], message="operation falied", start_time=start_time))


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
            message = db.get_all(query)
            if give_hash(input['password']) == message[0][0]:
                print("HELLO")
                access_token = create_access_token(identity=input['email'])
                return jsonify(give_response_access_token(data=[], message="login successful",access_token=access_token, start_time=start_time))
            else:
                return jsonify(give_response(data=[], message="wrong username or password", start_time=start_time))
    else:
        return jsonify({ "message" : v })

