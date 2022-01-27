from cmath import log
from os import access
from flask import request, jsonify
from Utilities.db_operations import *
from Utilities.error_handler import custom_response_maker
from .validation import *
import hashlib
from flask_jwt_extended import create_access_token, decode_token


def create_user():
    body = {}
    body = request.get_json()

    if(isinstance(validate_insert(body), dict)):
        return custom_response_maker(validate_insert(body))

    plaintext = hashlib.md5(body['password'].encode())
    hashed_password = plaintext.hexdigest()
    try:
        query = 'INSERT INTO Students VALUES (%d , "%s" , "%s" , "%s" );' % (
                body['id'], body['username'], body['email'], hashed_password)
    except KeyError as e:
        remodeled_err = {
            'err_code': 'Key Error',
            'message': 'Key error requires %s key' % (e.args[0])
        }
        return custom_response_maker(remodeled_err)
    return custom_response_maker(insert_row(query))


def show_users():
    if authorize(request):
        try:
            query = 'SELECT * FROM Students'
        except KeyError as e:
            remodeled_err = {
                'err_code': 'Key Error',
                'message': 'Key error requires %s key' % (e.args[0])
            }
            return custom_response_maker(remodeled_err)
        return custom_response_maker(read_row(query))
    else:
        return { "msg" : "unauthorized user"}



def login_user():
    body = {}
    body = request.get_json()

    if(isinstance(validate_login(body), dict)):
        return custom_response_maker(validate_login(body))

    try:
        query = 'SELECT password FROM Students WHERE username="%s"' % (
            body['username'])
    except KeyError as e:
        remodeled_err = {
            'err_code': 'Key Error',
            'message': 'Key error requires %s key' % (e.args[0])
        }
        return custom_response_maker(remodeled_err)

    res = read_row(query)
    login_res = validate_password(res['data'][0]['password'],body)
    if login_res["is_success"]:
        access_token = create_access_token(identity=body['username'])
        return access_token
    else:
        return login_res


def authorize(req):
    try:
        token = req.headers['AUTHORIZATION'].split(' ')[1]
    except KeyError as e:
        print(req.headers)
        return False
    username = decode_token(token)['sub']

    query = 'SELECT username FROM Students WHERE username="%s";'%(username)
    data= read_row(query)
    db_user = data['data'][0]['username']

    if db_user == username:
        return True
    else:
        return False