from flask import Blueprint
from Students.controller import *

students_bp = Blueprint('students_bp',__name__)

students_bp.route("/getAll",methods=['GET']) (get_all_students)

students_bp.route("/get",methods=['GET']) (get_specific_student)

students_bp.route("/post",methods=['POST']) (insert_student)

students_bp.route("/update",methods=['PATCH']) (update_student)

students_bp.route("/delete",methods=['DELETE']) (del_student)

students_bp.route("/login",methods=['POST']) (login)
