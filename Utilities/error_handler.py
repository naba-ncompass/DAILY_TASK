from email import message
from pyexpat.errors import messages
from flask import Blueprint, json, jsonify
import json
from werkzeug.exceptions import HTTPException
import json

bp_errors = Blueprint('bp_errors',__name__)
@bp_errors.app_errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        response = {
            "success":False,
            "code": e.code,
            "name": e.name,
            "data": [],
            "message": e.description
        }
        return jsonify(response)
    # elif isinstance(e, KeyError):
    #     if e.args[0] == 'HTTP_AUTHORIZATION':
    #         response = {
    #             "success":False,
    #             "data": [],
    #             "message": f"you are not logged in !!!!"
    #         }
    #     else:
    #         response = {
    #             "success":False,
    #             "data": [],
    #             "message": f"Trying to access key {e.args} which does not exists !!"
    #         }
    #     return jsonify(response)
    # else:
    #     response = {
    #         "success":False,
    #         "data": [],
    #         "message": "something went wrong!!!"
    #     }
    #     return response

def generate_error_response(e):

    response = {
        "success":False,
        "data":[],
        "message": e.msg
    }
    return jsonify(response)