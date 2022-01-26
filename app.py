from flask import Flask,jsonify,request
import json
from Utilities import db,error_handler,compression
from Employee.route import bp
from Device.route import device_routes
from flask import make_response, json ,Response
import gzip

app = Flask(__name__)

app.register_blueprint(bp)       
#  IF YOU WANT TO RUN EMPLOYEE DATABASE

app.register_blueprint(device_routes)
app.register_blueprint(error_handler.bp_errors)


if __name__ == '__main__':
    app.env = 'development'
    app.run(host='0.0.0.0',port='8004',debug=True)