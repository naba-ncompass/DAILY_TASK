from flask import Flask,jsonify,request
import json
from Utilities import db,error_handler
from Employee import route

app = Flask(__name__)

app.register_blueprint(route.bp)
app.register_blueprint(error_handler.bp_errors)

if __name__ == '__main__':
    app.env = 'development'
    app.run(debug=True)