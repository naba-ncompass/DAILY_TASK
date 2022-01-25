from flask import Blueprint
from Student import controller

student_routes = Blueprint('student_routes', __name__)

student_routes.route('/')(controller.read_operation)

student_routes.route('/read')(controller.read_where_operation)

student_routes.route("/insert", methods=['POST'])(controller.insert_operation)

student_routes.route("/update", methods=['PUT'])(controller.update_operation)

student_routes.route("/delete", methods=['DELETE'])(controller.delete_operation)

student_routes.route("/login", methods=['POST'])(controller.student_login)
