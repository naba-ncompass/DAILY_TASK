from flask import Flask,jsonify,request
import json
import db

app = Flask(__name__)

@app.route("/")
def hello_world():
    var = db.read_from_student()
    json_output = json.dumps(var)
    return jsonify(var)

@app.route("/insert", methods=['POST'])
def insert_operation():
    input_data = {}
    input_data = request.get_json()
    
    return 'hello'
