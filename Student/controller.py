from flask import jsonify, request
from flask_jwt_extended import create_access_token, decode_token
from datetime import datetime
from Utilities import db, error_handler
from Student import validation
import hashlib


def add_quotes(data, value):
    if data == 'cgpa':
        return value
    else:
        return f'\'{value}\''


def get_user_from_token():
    token = str(request.headers['Authorization']).split(' ')[1]
    return decode_token(token)['sub']


def check_user():
    username = get_user_from_token()
    query = f"select count(*) from student where username = '{username}'"
    output = db.read_from_table(query)
    if output[0][0] == 1:
        return True
    else:
        return "user not found"


def give_hash(input):
    hash = hashlib.md5(input.encode())
    return hash.hexdigest()


def read_from_student():
    if isinstance(check_user(), bool):
        start_time = datetime.now()
        query = f"select * from student"
        output = db.read_from_table(query)
        return jsonify(
            db.give_response(data=output,
                             message='operation successful',
                             start_time=start_time))
    else:
        return jsonify(error_handler.generate_error_response(check_user()))


def read_by_id_student():
    if isinstance(check_user(), bool):
        id = request.args['id']
        start_time = datetime.now()
        validity = validation.validate_read(id)
        if isinstance(validity, bool):
            query = f"select * from student where id = '{id}'"
            output = db.read_from_table(query)
            return jsonify(
                db.give_response(data=output,
                                 message='operation successful',
                                 start_time=start_time))
        else:
            return jsonify(error_handler.generate_error_response(validity))
    else:
        return jsonify(error_handler.generate_error_response(check_user()))


def insert_in_student():
    if isinstance(check_user(), bool):
        start_time = datetime.now()
        input_data = {}
        input_data = request.get_json()
        validity = validation.validate_insert(input_data)
        if isinstance(validity, bool):
            query = f"insert into student values ('{input_data['id']}', '{input_data['name']}', '{input_data['department']}', {input_data['cgpa']}, '{input_data['username']}', '{input_data['password']}')"
            message = db.insert_into_table(query)
            return jsonify(
                db.give_response(data=[],
                                 message=message,
                                 start_time=start_time))
        else:
            return jsonify(error_handler.generate_error_response(validity))
    else:
        return jsonify(error_handler.generate_error_response(check_user()))


def update_in_student():
    if isinstance(check_user(), bool):
        start_time = datetime.now()
        input_data = {}
        input_data = request.get_json()
        validity = validation.validate_update(input_data)
        if isinstance(validity, bool):
            new_value = add_quotes(input_data['change_col'],
                                   input_data['new_value'])
            where_value = add_quotes(input_data['where_col'],
                                     input_data['where_value'])
            query = f"update student set {input_data['change_col']} = {new_value} where {input_data['where_col']} = {where_value}"
            message = db.update_table(query)
            return jsonify(
                db.give_response(data=[],
                                 message=message,
                                 start_time=start_time))
        else:
            return jsonify(error_handler.generate_error_response(validity))
    else:
        return jsonify(error_handler.generate_error_response(check_user()))


def delete_from_student():
    if isinstance(check_user(), bool):
        start_time = datetime.now()
        input_data = {}
        input_data = request.get_json()
        validity = validation.validate_delete(input_data)
        if isinstance(validity, bool):
            where_value = add_quotes(input_data['where_col'],
                                     input_data['where_value'])
            query = f"delete from student where {input_data['where_col']} = {where_value}"
            message = db.delete_from_table(query)
            return jsonify(
                db.give_response(data=[],
                                 message=message,
                                 start_time=start_time))
        else:
            return jsonify(error_handler.generate_error_response(validity))
    else:
        return jsonify(error_handler.generate_error_response(check_user()))


def student_login():

    start_time = datetime.now()
    input_data = {}
    input_data = request.get_json()
    validity = validation.validate_insert(input_data)

    if isinstance(validity, bool):
        query = f"select password from student where username = '{input_data['username']}'"
        store_password = db.read_from_table(query)

        if give_hash(input_data['password']) == store_password[0][0]:
            access_token = create_access_token(identity=input_data['username'])
            return jsonify(
                db.give_response(data=[],
                                 message="login successfull !!!",
                                 start_time=start_time,
                                 token=access_token))
        else:
            return jsonify(
                db.give_response(data=[],
                                 message="wrong username or password !!",
                                 start_time=start_time))
    else:
        return jsonify(error_handler.generate_error_response(validity))
