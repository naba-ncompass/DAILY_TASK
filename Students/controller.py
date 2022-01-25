from flask import request, jsonify
from Utilities.db_operations import *
from Utilities.error_handler import custom_response_maker
from .validation import *
import hashlib


def create_user():
    body = {}
    body = request.get_json()

    if(isinstance(validate_insert(body), dict)):
        return custom_response_maker(validate_insert(body))

    # hashing password
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
    try:
        query = 'SELECT * FROM Students'
    except KeyError as e:
        remodeled_err = {
            'err_code': 'Key Error',
            'message': 'Key error requires %s key' % (e.args[0])
        }
        return custom_response_maker(remodeled_err)
    return custom_response_maker(read_row(query))


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

    # retrieving password from db
    res = read_row(query)
    user_password = res['data'][0]['password']

    # hashing password from user to compare
    plaintext = hashlib.md5(body['password'].encode())
    hashed_password = plaintext.hexdigest()

    if user_password == hashed_password:
        return jsonify({
            "message": "user : %s is logged in" % (body['username'])
        })
    else:
        return jsonify({
            "message": "user : %s password is wrong" % (body['username'])
        })
