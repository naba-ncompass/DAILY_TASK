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

def generate_error_response(e):

    response = {
        "success":False,
        "data":[],
        "message": e.msg
    }
    return jsonify(response)