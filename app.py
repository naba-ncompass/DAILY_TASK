from crypt import methods
from urllib import response
from flask import Flask, jsonify, request
from db_operations import *


app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>This is the Home Page</p1>"

@app.route("/read_shows", methods=['GET'])
def read_from_db():
    data = read_row()
    return jsonify(data)

@app.route("/create_show",methods=['POST'])
def insert_to_db():
    body = {}
    body = request.get_json()
    response = insert_row(body)
    return jsonify(response)

@app.route("/update_show",methods=['PUT'])
def update_to_db():
    body = {}
    body = request.get_json()
    response = update_row(body)
    return jsonify(response)

@app.route("/delete_show", methods=['DELETE'])
def delete_from_db():
    body = {}
    body = request.get_json()
    response = delete_row(body)
    return jsonify(response)



if __name__  == "__main__":
    app.env = "development"
    app.run()

