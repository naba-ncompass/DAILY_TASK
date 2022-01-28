from flask import Blueprint
from Student import controller

student_routes = Blueprint('student_routes', __name__)

student_routes.route('/')(controller.read_from_student)

student_routes.route('/read')(controller.read_by_id_student)

student_routes.route("/insert", methods=['POST'])(controller.insert_in_student)

student_routes.route("/update", methods=['PUT'])(controller.update_in_student)

student_routes.route("/delete",
                     methods=['DELETE'])(controller.delete_from_student)

student_routes.route("/login", methods=['POST'])(controller.student_login)
