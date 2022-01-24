from flask import jsonify , request
from Utilities.db_operations import *

def custom_response_maker(res):
    message = ''
    is_success = False

    if 'err_code' in res:
        print("response in crm: ",res)
        return jsonify({
            "is_success" : is_success,
            "data" : None,
            "message": res['message'],
            "start_time": None,
            "end_time": None,
            "duration": None
        })
    elif isinstance(res["data"],int):
        message = "no of rows changed : %d"%(res["data"])
        is_success = True
    elif isinstance(res["data"],list):
        is_success = True

    return jsonify({
        "is_success" : is_success,
        "data" : res["data"],
        "message": message,
        "start_time": res["start_time"],
        "end_time": res["end_time"],
        "duration": res["end_time"] - res["start_time"]
    })
    
def home():
    return "<h1>This is the First Page</p1>"

def read_from_db():
    query = 'SELECT * FROM TvShows'
    return custom_response_maker(read_row(query))

def insert_to_db():
    body = {}
    body = request.get_json()
    try:
        query = 'INSERT INTO TvShows VALUES (%d , "%s" , "%s" );'%(
                body['id'], body['name'], body['studio'])
    except KeyError as e:
        remodeled_err = {
            'err_code': 'Key Error',
            'message': 'Key error requires %s key'%(e.args[0])
        }
        return custom_response_maker(remodeled_err)
    return custom_response_maker(insert_row(query))

def update_to_db():
    body = {}
    body = request.get_json()
    try:
        query = 'UPDATE TvShows SET %s="%s" WHERE id = %d;'%(
                body['column'], body['new_value'], body['id'])
    except KeyError as e:
        remodeled_err = {
            'err_code': 'Key Error',
            'message': 'Key error requires %s key'%(e.args[0])
        }
        return custom_response_maker(remodeled_err)
    return custom_response_maker(update_row(query))

def delete_from_db():
    body = {}
    body = request.get_json()
    try:
        query = 'DELETE FROM TvShows WHERE id = %d ;'%(body['id'])
    except KeyError as e:
      #print("KEY ERROR RESPONSE: ",e.args)
      #print(dir(e))
        remodeled_err = {
            'err_code': 'Key Error',
            'message': 'Key error requires %s key'%(e.args[0])
        }
        return custom_response_maker(remodeled_err)
    return custom_response_maker(delete_row(query))

