from flask import Blueprint
from Device import controller

device_routes = Blueprint('device_routes', __name__)

device_routes.route('/device_read')(controller.read_operation)

device_routes.route('/peak', methods=['POST'])(controller.peak_between_times)

device_routes.route("/sum")(controller.sum_between_times)

device_routes.route("/duplicate")(controller.duplicate_between_times)

