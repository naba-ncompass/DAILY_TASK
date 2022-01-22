from flask import jsonify , request
from Utilities.db import *

def create_Result(data,func_name):
    result = {}
    result['isSuccess'] = True
    if(func_name =='get_all_records'):
        result['data'] = data
        result['message'] = 'Read all records' if(data!=None) else "No record/s"
    elif(func_name =='get_record'):
        result['data'] = data
        result['message'] = 'Read specific record' if(data!=None) else "No record"
    elif(func_name == 'post_record'):
        result['message'] = f"{data} row inserted"
    elif(func_name == 'patch_record'):
        result['message'] = f"{data} row updated"
    else:
        result['message'] = f"{data} row deleted"
    return result

def get_all_records():
    sql_command = "SELECT * FROM students"
    data = read_all_records(sql_command)
    result = create_Result(data,"get_all_records")
    return jsonify(result)

def get_record(id):
    sql_command = f"SELECT * FROM students WHERE ID = {id}"
    data = read_specific_record(sql_command)
    result = create_Result(data,"get_record")
    return jsonify(result)

def post_record():
    body = {}
    body = request.get_json()
    _id = body['id']
    name = body['name']
    dept = body['dept']

    sql_command = f"INSERT into students (id,name,dept) values ({_id},'{name}','{dept}')"

    data = create_single_record(sql_command)
    result = create_Result(data,"post_record")
    return jsonify(result)

def patch_record(id):
    body = {}
    body = request.get_json()

    for key in body.keys():
        column_name = key
        value = body[key]
    _id = id

    sql_command = f"UPDATE students SET {column_name} = '{value}' WHERE ID = {_id}"

    data = update_record(sql_command)
    result = create_Result(data,"patch_record")
    return jsonify(result)

def del_record(id):
    sql_command = f"DELETE FROM students WHERE ID = {id}"
    data = delete_record(sql_command)
    result = create_Result(data,"del_record")
    return jsonify(result)