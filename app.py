from flask import Flask,jsonify,request
import json
import db

app = Flask(__name__)

@app.route("/")
def hello_world():
    var = db.get_all()
    return jsonify(var)

@app.route("/insert", methods=['POST'])
def insert_operation():
    input_data = {}
    input_data = request.get_json()
    msg = db.insert(input_data)
    return msg


@app.route("/update", methods=['PUT'])
def update_operation():
    input_data = {}
    input_data = request.get_json()
    msg = db.update(input_data)
    return msg

@app.route("/delete", methods=['DELETE'])
def delete_operation():
    input_data = {}
    input_data = request.get_json()
    msg = db.delete(input_data)
    return msg

if __name__ == '__main__':
    app.env = 'development'
    app.run()