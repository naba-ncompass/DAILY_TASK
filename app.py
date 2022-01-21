from flask import Flask,jsonify,request
import json
import db

app = Flask(__name__)

@app.route("/")
def read_operation():
    var = db.read_from_student()
    json_output = json.dumps(var)
    return jsonify(var)

@app.route("/insert", methods=['POST'])
def insert_operation():
    input_data = {}
    input_data = request.get_json()
    response = db.insert_into_student(input_data)
    return response

@app.route("/update", methods=['PUT'])
def update_operation():
    input_data = {}
    input_data = request.get_json()
    response = db.update_student(input_data)
    return response

@app.route("/delete", methods=['DELETE'])
def delete_operation():
    input_data = {}
    input_data = request.get_json()
    response = db.delete_from_student(input_data)
    return response

if __name__ == '__main__':
    app.env = 'development'
    app.run()