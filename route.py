from flask import Flask,jsonify,request,Blueprint
from Utilities.db import *
from Employee.controller import *
bp = Blueprint("bp",__name__)

@bp.route("/")
def hello_world():
    return "<H1>NCOMPASS<H1>"

# @bp.route("/read", methods=['GET'])
# def read_operation():
#     response = db.get_all()
#     return jsonify(response)


bp.route("/read", methods=['GET'])(show_item)

bp.route("/insert", methods=['POST'])(insert_operation)

# bp.route("/update", methods=['PUT'])(controller.update_operation)

bp.route("/update", methods=['PUT'])(update_operation)

bp.route("/delete", methods=['DELETE'])(delete_operation)

bp.route("/truncate", methods=['DELETE'])(truncate_operation)

# bp.route("/create", methods=['POST'])(create_operation)
