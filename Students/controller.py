from flask import request,Response
from Utilities.db import *
from Students.validation import *
from Utilities.error_handler import validation_err
from Utilities.compression import *
import hashlib
import time
from flask_jwt_extended import create_access_token,decode_token

def create_result(data,func_name):
    result = {}
    result['isSuccess'] = True
    result['data'] = data
    if(func_name =='get_all_students'):
        result['message'] = 'Read all records' if(data!=None) else "No record/s"
    elif(func_name =='get_specific_student'):
        result['message'] = 'Read specific record' if(data!=None) else "No record"
    elif(func_name == 'insert_student'):
        result['message'] = f"{data} row inserted"
    elif(func_name == 'update_student'):
        result['message'] = f"{data} row updated"
    elif(func_name == 'del_student'):
        result['message'] = f"{data} row deleted"
    else:
        result['message'] = f"User Accepted" if(data[0]!=0) else "No record, check username or password"
    return result


def create_response(result,start_time,end_time):
    result['start_time_sec'] = start_time
    result['end_time_sec'] = end_time
    result['duration_sec'] = result['end_time_sec'] - result['start_time_sec']
    result['duration_ms'] = int(result['duration_sec']*1000)
    compressed_result = create_compression(result)
    response = Response(compressed_result,
        content_type="application/json"
    )
    response.content_encoding = 'gzip'
    return response


def hash_value(password):
    hash = hashlib.md5(password.encode())
    return hash.hexdigest()

def check_authorisation(username):
    sql_connector= create_connection()
    cursor = sql_connector.cursor()
    sql_query= f"SELECT EXISTS (SELECT username FROM students WHERE username = '{username}')"
    cursor.execute(sql_query)
    output_auth = cursor.fetchone()[0]
    close_connection(sql_connector)
    return output_auth


def get_all_students():
    start_time = time.perf_counter()
    auth = str(request.headers['Authorization'].split(' ')[1])
    username = decode_token(auth)['sub']
    output_auth = check_authorisation(username)
    if(output_auth==1):
        sql_query = "SELECT * FROM students"
        data = read_all(sql_query)
        result = create_result(data,"get_all_students")
        end_time = time.perf_counter()
        response = create_response(result,start_time,end_time)
        return response
    return Response("wrong token",content_type="application/json")


def get_specific_student():
    start_time = time.perf_counter()
    auth = str(request.headers['Authorization'].split(' ')[1])
    username = decode_token(auth)['sub']
    output_auth = check_authorisation(username)
    if(output_auth==1):
        params = request.args
        if isinstance(check_get(params),bool) and check_get(params)==True:
            sql_query = f"SELECT * FROM students WHERE ID = {int(params['id'])}"
            data = read_specific(sql_query)
            result = create_result(data,"get_specific_student")
            end_time = time.perf_counter()
            response = create_response(result,start_time,end_time)
            return response

        return validation_err(check_get(params))
    return Response("wrong token",content_type="application/json")
    

def insert_student():
    start_time = time.perf_counter()
    auth = str(request.headers['Authorization'].split(' ')[1])
    username = decode_token(auth)['sub']
    output_auth = check_authorisation(username)
    if(output_auth==1):
        body = {}
        body = request.get_json()
        _id = body['id']
        name = body['name']
        dept = body['dept']
        username = body['username']
        password = body['password']
        pass_digest = hash_value(password)
        if isinstance(check_post(body),bool) and check_post(body)==True:
            sql_query = f"INSERT into students (id,name,dept,username,password) values ({_id},'{name}','{dept}','{username}','{pass_digest}')"
            data = create(sql_query)
            result = create_result(data,"insert_student")
            end_time = time.perf_counter()
            response = create_response(result,start_time,end_time)
            return response
        return validation_err(check_post(body)) 
    return Response("wrong token",content_type="application/json")


def update_student():
    start_time = time.perf_counter()
    auth = str(request.headers['Authorization'].split(' ')[1])
    username = decode_token(auth)['sub']
    output_auth = check_authorisation(username)
    if(output_auth==1):
        body = {}
        body = request.get_json()
        for key in body.keys():
            column_name = key
            value = body[key]
        params = request.args
        body['id']=params['id']
        _id = body['id']
        if isinstance(check_patch(body),bool) and check_patch(body)==True:
            sql_query = f"UPDATE students SET {column_name} = '{value}' WHERE ID = {int(_id)}"
            data = update(sql_query)
            result = create_result(data,"update_student")
            end_time = time.perf_counter()
            response = create_response(result,start_time,end_time)
            return response
        return validation_err(check_patch(body)) 
    return Response("wrong token",content_type="application/json")
    

def del_student():
    start_time = time.perf_counter()
    auth = str(request.headers['Authorization'].split(' ')[1])
    username = decode_token(auth)['sub']
    output_auth = check_authorisation(username)
    if(output_auth==1):
        params = request.args
        _id = params['id']
        if isinstance(check_delete(params),bool) and check_delete(params)==True:
            sql_query = f"DELETE FROM students WHERE ID = {int(_id)}"
            data = delete(sql_query)
            result = create_result(data,"del_student")
            end_time = time.perf_counter()
            response = create_response(result,start_time,end_time)
            return response
        return validation_err(check_delete(params))
    return Response("wrong token",content_type="application/json")
    

def login():
    start_time = time.perf_counter()
    body = {}
    body = request.get_json()
    username = body['username']
    password = body['password']
    pass_digest = hash_value(password)
    if isinstance(check_login(body),bool) and check_login(body)==True:
        sql_query = f"SELECT EXISTS (SELECT * FROM students WHERE username = '{username}' and password = '{pass_digest}')"
        data = check_record(sql_query)
        result = create_result(data,"login")
        if(data[0]!=0):
            access_token = create_access_token(identity=username)
            result['access_token'] = access_token
        end_time = time.perf_counter()
        response = create_response(result,start_time,end_time)
        return response

    return validation_err(check_login(body))