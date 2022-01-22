from flask import Blueprint
from Students.controller import *

app_bp = Blueprint('app_bp',__name__)

app_bp.route("/getAll",methods=['GET']) (get_all_records)

app_bp.route("/get/<int:id>",methods=['GET']) (get_record)

app_bp.route("/post",methods=['POST']) (post_record)

app_bp.route("/update/<int:id>",methods=['PATCH']) (patch_record)

app_bp.route("/delete/<int:id>",methods=['DELETE']) (del_record)
