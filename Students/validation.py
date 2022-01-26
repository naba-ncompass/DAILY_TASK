from cerberus import Validator
from flask import jsonify
import hashlib

v = Validator()

def parse_err(errors):
    message = ''
    for errs in errors:
        message = message + '%s %s , ' % (errs, v.errors[errs][0])
    return message

def validate_insert(body):
    schema = {
        'id': {'type': 'integer'},
        'username': {'type': 'string','maxlength': 25},
        'email': {
            'type': 'string',
            'maxlength': 25,
            'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$' },
        'password': { 'type': 'string', 'maxlength': 50}
    }

    if v.validate(body, schema):
        return True
    else:
        return {
            "err_code": "Validation Error",
            "message": parse_err(v.errors)
        }


def validate_login(body):
    schema = {
        'username': {
            'type': 'string',
            'maxlength': 25
        },
        'password': { 'type': 'string', 'maxlength': 50}
    }

    if v.validate(body, schema):
        return True
    else:
        return {
            "err_code": "Validation Error",
            "message": parse_err(v.errors)
        }

def validate_password(user_password,res_body):

    # hashing password from user to compare
    plaintext = hashlib.md5(res_body['password'].encode())
    hashed_password = plaintext.hexdigest()

    if user_password == hashed_password:
        return jsonify({
            "message": "user : %s is logged in" % (res_body['username'])
        })
    else:
        return jsonify({
            "message": "user : %s password is wrong" % (res_body['username'])
        })