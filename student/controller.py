from flask import jsonify,request
from timeit import default_timer as timer
from datetime import datetime,timedelta
from Utilities import db
import json

def read_operation():
    start_time = datetime.now()
    query = "select * from student"
    var = db.read_from_student(query)
    return jsonify(give_response(data=var, message='operation successful', start_time=start_time))

def insert_operation():
    start_time = datetime.now()
    input_data = {}
    input_data = request.get_json()
    query = f"insert into student values ('{input_data['id']}', '{input_data['name']}', '{input_data['department']}', {input_data['cgpa']})"
    message = db.insert_into_student(query)
    return jsonify(give_response(data=[], message=message, start_time=start_time))

def update_operation():
    start_time = datetime.now()
    input_data = {}
    input_data = request.get_json()
    new_value = check_value(input_data['change_col'],input_data['new_value'])
    where_value = check_value(input_data['where_col'],input_data['where_value'])
    query = f"update student set {input_data['change_col']} = {new_value} where {input_data['where_col']} = {where_value}"
    message = db.update_student(query)
    return jsonify(give_response(data=[], message=message, start_time=start_time))

def delete_operation():
    start_time = datetime.now()
    input_data = {}
    input_data = request.get_json()
    where_value = check_value(input_data['where_col'],input_data['where_value'])
    query = f"delete from student where {input_data['where_col']} = {where_value}"
    message = db.delete_from_student(query)
    return jsonify(give_response(data=[], message=message, start_time=start_time))

def check_value(data,value):
    if data == 'cgpa':
        return value
    else:
        return f'\'{value}\''

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