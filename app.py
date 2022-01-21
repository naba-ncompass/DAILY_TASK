from flask import Flask,jsonify,request
from db import *

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Welcome Home Page!</h1>"
    

@app.route("/getRecords",methods=['GET'])
def get_all_records():
    records = read_all_records()
    return jsonify(records)


@app.route("/getRecords/<int:id>",methods=['GET'])
def get_record(id):
    record = read_specific_record(id)
    return jsonify(record)


@app.route("/postRecord",methods=['POST'])
def post_record():
    body = {}
    body = request.get_json()

    result = create_single_record(body)
    res = jsonify(result)
    return res


@app.route("/updateRecord/<int:id>",methods=['PATCH'])
def patch_record(id):
    body = {}
    body = request.get_json()

    record = {}
    for key in body.keys():
        record['column_name'] = key
        record['value'] = body[key]
    record['id'] = id

    result = update_record(record)
    res = jsonify(result)
    return res


@app.route("/deleteRecord/<int:id>",methods=['DELETE'])
def del_record(id):
    result = delete_record(id)
    res = jsonify(result)
    return res


    





if __name__ == '__main__':
    app.env='development'
    app.run(debug=True)