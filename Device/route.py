from flask import Flask,jsonify,request,Blueprint
from Device import controller
device_routes = Blueprint("device_routes",__name__)

@device_routes.route("/")
def hello_world():
    return "<H1>NCOMPASS<H1>"

device_routes.route("/reads")(controller.reads_device)

device_routes.route("/sum")(controller.sum_device)

device_routes.route("/peak")(controller.peak_device)

device_routes.route("/duplicate")(controller.duplicate_device)