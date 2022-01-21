from flask import Blueprint,jsonify
from Utilities import db
import json
from Student import controller

bp_routes = Blueprint('bp_routes', __name__)

bp_routes.route('/')(controller.read_operation)

bp_routes.route("/insert", methods=['POST'])(controller.insert_operation)

bp_routes.route("/update", methods=['PUT'])(controller.update_operation)

bp_routes.route("/delete", methods=['DELETE'])(controller.delete_operation)
