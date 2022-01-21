from flask import Flask,jsonify,request
from route import bp
import json
import db

app = Flask(__name__)

app.register_blueprint(bp)

if __name__ == '__main__':
    app.env = 'development'
    app.run()