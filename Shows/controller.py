from flask import jsonify , request
from Utilities.db_operations import *

def home():
    return "<h1>This is the First Page</p1>"

def read_from_db():
    query = 'SELECT * FROM TvShows'
    return jsonify(read_row(query))

def insert_to_db():
    body = {}
    body = request.get_json()
    query = 'INSERT INTO TvShows VALUES (%d , "%s" , "%s" );'%(
            body['id'], body['name'], body['studio'])
    response = insert_row(query)
    return jsonify(response)

def update_to_db():
    body = {}
    body = request.get_json()
    query = 'UPDATE TvShows SET %s="%s" WHERE id = %d;'%(
            body['column'], body['new_value'], body['id'])
    response = update_row(query)
    return jsonify(response)

def delete_from_db():
    body = {}
    body = request.get_json()
    query = 'DELETE FROM TvShows WHERE id = %d ;'%(body['id'])
    response = delete_row(query)
    return jsonify(response)
