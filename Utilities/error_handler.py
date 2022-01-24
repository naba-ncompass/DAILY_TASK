from flask import Blueprint,Response
from werkzeug.exceptions import HTTPException
from mysql.connector import Error
import json


err = Blueprint('err',__name__)

@err.app_errorhandler(Exception)
def handle_exception(e):
    if isinstance(e,HTTPException): 
        response = e.get_response()
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
            "data":[]
        })
        response.content_type = "application/json"
        return response,200

    elif isinstance(e,Error): 
        return Response(json.dumps({
            "code": e.errno,
            "name":"Mysql Error",
            "description": e.msg,
            "data":[]
        }),content_type="application/json"),200

    return Response(json.dumps({
        "code": 500,
        "name":e.__class__.__name__,
        "description": str(e.args),
        "data":[]
    }),content_type="application/json"),200

def validation_err(e):
    return Response(json.dumps({
            "name":"Validation Error",
            "description": str(e),
            "data":[]
        }),content_type="application/json"),200

