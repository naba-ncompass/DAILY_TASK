from flask import Blueprint
from Students.controller import *

students_bp = Blueprint('students_bp',__name__)

students_bp.route("/getAll",methods=['GET']) (get_all_records)

students_bp.route("/get",methods=['GET']) (get_record)

students_bp.route("/post",methods=['POST']) (post_record)

students_bp.route("/update",methods=['PATCH']) (patch_record)

students_bp.route("/delete",methods=['DELETE']) (del_record)
