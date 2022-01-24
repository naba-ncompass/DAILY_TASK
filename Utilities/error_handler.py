import json
from werkzeug.exceptions import HTTPException , BadRequest
from flask import Blueprint , jsonify

err_bp = Blueprint('err_bp',__name__)


@err_bp.app_errorhandler(HTTPException)
def handle_exception(e):
    response = {
        "err_code": e.code,
        "message": e.description,
    }
    return custom_reponse_maker(response)


@err_bp.app_errorhandler(BadRequest)
def handle_badrequest(e):
    response = {
        "err_code": e.code,
        "message": e.description,
    }
    return custom_response_maker(response)

def custom_response_maker(res):
    message = ''
    is_success = False

    if 'err_code' in res:
        print("response in crm: ",res)
        return jsonify({
            "is_success" : is_success,
            "data" : None,
            "message": res['message'],
            "start_time": None,
            "end_time": None,
            "duration": None
        })
    elif isinstance(res["data"],int):
        message = "no of rows changed : %d"%(res["data"])
        is_success = True
    elif isinstance(res["data"],list):
        is_success = True

    return jsonify({
        "is_success" : is_success,
        "data" : res["data"],
        "message": message,
        "start_time": res["start_time"],
        "end_time": res["end_time"],
        "duration": res["end_time"] - res["start_time"]
    })
    
def generate_response(e):
    return {
        "err_code" : e.args[0], 
        "message" : e.args[1],
        "err_type": e.__class__
        }