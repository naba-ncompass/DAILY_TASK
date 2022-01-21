from flask import Flask,jsonify,request
from Student import route
import json
from Utilities import db,error_handler
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

app.register_blueprint(route.bp_routes)
app.register_blueprint(error_handler.bp_errors)


if __name__ == '__main__':
    app.env = 'development'
    app.debug = True
    app.run()