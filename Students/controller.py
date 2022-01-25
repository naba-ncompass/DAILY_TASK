from flask import jsonify , request
from Utilities.db import *
from Students.validation import *
from Utilities.error_handler import validation_err
import hashlib

def create_Result(data,func_name):
    result = {}
    result['isSuccess'] = True
    result['data'] = data
    if(func_name =='get_all_records'):
        result['message'] = 'Read all records' if(data!=None) else "No record/s"
    elif(func_name =='get_record'):
        result['message'] = 'Read specific record' if(data!=None) else "No record"
    elif(func_name == 'post_record'):
        result['message'] = f"{data} row inserted"
    elif(func_name == 'patch_record'):
        result['message'] = f"{data} row updated"
    elif(func_name == 'del_record'):
        result['message'] = f"{data} row deleted"
    else:
        result['message'] = f"User Accepted" if(data[0]!=0) else "No record, check username or password"
    return result


def hash_value(password):
    hash = hashlib.md5(password.encode())
    return hash.hexdigest()


def get_all_records():
    sql_command = "SELECT * FROM students"
    data = read_all_records(sql_command)
    result = create_Result(data,"get_all_records")
    return jsonify(result)


def get_record():
    params = request.args
    if isinstance(check_get(params),bool) and check_get(params)==True:
        sql_command = f"SELECT * FROM students WHERE ID = {int(params['id'])}"
        data = read_specific_record(sql_command)
        result = create_Result(data,"get_record")
        return jsonify(result)

    return validation_err(check_get(params))
    

def post_record():
    body = {}
    body = request.get_json()
    _id = body['id']
    name = body['name']
    dept = body['dept']
    username = body['username']
    password = body['password']
    pass_digest = hash_value(password)

    if isinstance(check_post(body),bool) and check_post(body)==True:
        sql_command = f"INSERT into students (id,name,dept,username,password) values ({_id},'{name}','{dept}','{username}','{pass_digest}')"
        data = create_single_record(sql_command)
        result = create_Result(data,"post_record")
        return jsonify(result)

    return validation_err(check_post(body)) #here validation.check return error dictionary

def patch_record():
    body = {}
    body = request.get_json()

    for key in body.keys():
        column_name = key
        value = body[key]
    
    params = request.args
    body['id']=params['id']
    _id = body['id']

    if isinstance(check_patch(body),bool) and check_patch(body)==True:
        sql_command = f"UPDATE students SET {column_name} = '{value}' WHERE ID = {int(_id)}"
        data = update_record(sql_command)
        result = create_Result(data,"patch_record")
        return jsonify(result)

    return validation_err(check_patch(body)) 
    

def del_record():
    params = request.args
    _id = params['id']
    if isinstance(check_delete(params),bool) and check_delete(params)==True:
        sql_command = f"DELETE FROM students WHERE ID = {int(_id)}"
        data = delete_record(sql_command)
        result = create_Result(data,"del_record")
        return jsonify(result)

    return validation_err(check_delete(params))

def login_record():
    body = {}
    body = request.get_json()
    username = body['username']
    password = body['password']
    pass_digest = hash_value(password)

    if isinstance(check_login(body),bool) and check_login(body)==True:
        sql_command = f"SELECT EXISTS (SELECT * FROM students WHERE username = '{username}' and password = '{pass_digest}')"
        data = check_record_exists(sql_command)
        result = create_Result(data,"login_record")
        return jsonify(result)

    return validation_err(check_login(body))