from flask import jsonify , request
from Utilities.db_operations import *
from Utilities.error_handler import custom_response_maker
from .validation import *

def home():
    return "<h1>This is the First Page</p1>"

def read_from_db():
    if len(request.args)>0:
        req_params = request.args
        query = 'SELECT * FROM TvShows WHERE %s="%s"'%(req_params['column'],req_params['value'])
    else:
        query = 'SELECT * FROM TvShows'
    return custom_response_maker(read_row(query))

def insert_to_db():
    body = {}
    body = request.get_json()
    if (isinstance(validate_insert(body), dict)):
        return custom_response_maker(validate_insert(body))
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
    if (isinstance(validate_update(body), dict)):
        return custom_response_maker(validate_insert(body))
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
    if (isinstance(validate_delete(body), dict)):
        return custom_response_maker(validate_insert(body))
    try:
        query = 'DELETE FROM TvShows WHERE id = %d ;'%(body['id'])
    except KeyError as e:
        remodeled_err = {
            'err_code': 'Key Error',
            'message': 'Key error requires %s key'%(e.args[0])
        }
        return custom_response_maker(remodeled_err)
    return custom_response_maker(delete_row(query))

