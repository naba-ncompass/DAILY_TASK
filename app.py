from flask import Flask,jsonify,request
import json
from Employee.route import bp
from Utilities import db,error_handler,compression
from Device.route import device_routes
from flask import make_response, json ,Response
import gzip
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
app = Flask(__name__)

with open("Config/config.json",'r') as f:
            config = json.load(f)
app.config['JWT_SECRET_KEY'] = config['JWT_SECRET_KEY']  # you secret key keep it with you only!
jwt = JWTManager(app)

app.register_blueprint(bp)       
#  IF YOU WANT TO RUN EMPLOYEE DATABASE
app.register_blueprint(device_routes)
app.register_blueprint(error_handler.bp_errors)


if __name__ == '__main__':
    app.env = 'development'
    # app.run(host='0.0.0.0',port='8004',debug=True)
    # when i have to run in linux
    # app.run(host=app_config['host'],port=app_config['port'],debug=True)
    app.run(debug=True)