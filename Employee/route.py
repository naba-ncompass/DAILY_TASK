from flask import Flask,jsonify,request,Blueprint
from Utilities.db import *
from Employee.controller import *
bp = Blueprint("bp",__name__)

@bp.route("/")
def hello_world():
    return "<H1>NCOMPASS<H1>"

bp.route("/read", methods=['GET'])(read_employee)

bp.route("/readid", methods=['GET'])(read_employee_id)

bp.route("/insert", methods=['POST'])(insert_employee)

bp.route("/update", methods=['PUT'])(update_employee)

bp.route("/delete", methods=['DELETE'])(delete_employee)

bp.route("/truncate", methods=['DELETE'])(truncate_employee)

bp.route("/login", methods=['POST'])(student_login)