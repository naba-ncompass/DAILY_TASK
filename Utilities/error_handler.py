from flask import Blueprint,jsonify
from werkzeug.exceptions import HTTPException
import datetime

bp_errors = Blueprint('bp_errors', __name__)

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
    elif isinstance(e, KeyError):
        response = {
            "success":False,
            "data": [],
            "message": f"Trying to access key {e.args} which does not exists !!"
        }
        return jsonify(response)
    else:
        response = {
            "success":False,
            "data": [],
            "message": "something went wrong!!!"
        }
        return response


def generate_error_response(message):

    response = {
        "success":False,
        "data":[],
        "message": message
    }
    return response

def give_response(data,message,start_time):
    end_time = datetime.now()
    duration = end_time - start_time
    response = {
        "start_time": start_time.strftime("%H:%M:%S.%f"),
        "success": True,
        "data": data,
        "message":message,
        "end_time": end_time.strftime("%H:%M:%S.%f"),
        "duration":duration.total_seconds()
    }
    return response