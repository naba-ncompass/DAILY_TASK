from flask import Blueprint,jsonify
import db
import json
import controller

bp = Blueprint('bp', __name__)

bp.route('/')(controller.read_operation)

bp.route("/insert", methods=['POST'])(controller.insert_operation)

bp.route("/update", methods=['PUT'])(controller.update_operation)

bp.route("/delete", methods=['DELETE'])(controller.delete_operation)
