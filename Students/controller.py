from flask import jsonify , request
from Utilities.db import *
from Students.validation import *
from Utilities.error_handler import validation_err

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
    else:
        result['message'] = f"{data} row deleted"
    return result


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

    if isinstance(check_post(body),bool) and check_post(body)==True:
        sql_command = f"INSERT into students (id,name,dept) values ({_id},'{name}','{dept}')"
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