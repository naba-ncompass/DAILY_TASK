from flask import Blueprint
from Students.controller import *

app_bp = Blueprint('app_bp',__name__)

app_bp.route("/getAll",methods=['GET']) (get_all_records)

app_bp.route("/get",methods=['GET']) (get_record)

app_bp.route("/post",methods=['POST']) (post_record)

app_bp.route("/update",methods=['PATCH']) (patch_record)

app_bp.route("/delete",methods=['DELETE']) (del_record)
