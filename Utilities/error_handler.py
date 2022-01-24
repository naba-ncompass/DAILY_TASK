import json
from werkzeug.exceptions import HTTPException 
from flask import Blueprint , jsonify

err_bp = Blueprint('err_bp',__name__)

@err_bp.app_errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

def generate_response(e):
    return {
        "err_code" : e.args[0], 
        "message" : e.args[1],
        "err_type": e.__class__
        }