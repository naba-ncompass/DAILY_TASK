from flask import jsonify,request
import db
import json

def read_operation():
    query = "select * from student"
    var = db.read_from_student(query)
    json_output = json.dumps(var)
    return jsonify(var)

def insert_operation():
    input_data = {}
    input_data = request.get_json()
    query = f"insert into student values ('{input_data['id']}', '{input_data['name']}', '{input_data['department']}', {input_data['cgpa']})"
    response = db.insert_into_student(query)
    return response

def update_operation():
    input_data = {}
    input_data = request.get_json()
    new_value = check_value(input_data['change_col'],input_data['new_value'])
    where_value = check_value(input_data['where_col'],input_data['where_value'])
    query = f"update student set {input_data['change_col']} = {new_value} where {input_data['where_col']} = {where_value}"
    response = db.update_student(query)
    return response

def delete_operation():
    input_data = {}
    input_data = request.get_json()
    where_value = check_value(input_data['where_col'],input_data['where_value'])
    query = f"delete from student where {input_data['where_col']} = {where_value}"
    response = db.delete_from_student(query)
    return response

def check_value(data,value):
    if data == 'cgpa':
        return value
    else:
        return f'\'{value}\''