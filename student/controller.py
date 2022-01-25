from flask import jsonify,request
from datetime import datetime
from Utilities import db,error_handler
from Student import validation
import hashlib


def give_response(data,message,start_time):
    end_time = datetime.now()
    duration = end_time - start_time
    response = {
        "start_time": start_time.strftime("%H:%M:%S.%f"),
        "success": True,
        "data": data,
        "message":message,
        "end_time": end_time.strftime("%H:%M:%S.%f"),
        "duration":duration.total_seconds()
    }
    return response


def check_value(data,value):
    if data == 'cgpa':
        return value
    else:
        return f'\'{value}\''



def give_hash(input):
    hash = hashlib.md5(input.encode())
    return hash.hexdigest()


def read_operation():
    start_time = datetime.now()
    query = "select * from student"
    output = db.read_from_table(query)
    return jsonify(give_response(data=output, message='operation successful', start_time=start_time))


def read_where_operation():
    id = request.args['id']
    start_time = datetime.now()
    validity = validation.validate_read(id)
    if isinstance(validity, bool):
        query = f"select * from student where id = '{id}'"
        output = db.read_from_table(query)
        return jsonify(give_response(data=output, message='operation successful', start_time=start_time))
    else:
        return jsonify(error_handler.generate_error_response(validity))


def insert_operation():
    start_time = datetime.now()
    input_data = {}
    input_data = request.get_json()
    validity = validation.validate_insert(input_data)
    if isinstance(validity, bool):
        query = f"insert into student values ('{input_data['id']}', '{input_data['name']}', '{input_data['department']}', {input_data['cgpa']}, '{input_data['username']}', '{input_data['password']}')"
        message = db.insert_into_table(query)
        return jsonify(give_response(data=[], message=message, start_time=start_time))
    else:
        return jsonify(error_handler.generate_error_response(validity))


def update_operation():
    start_time = datetime.now()
    input_data = {}
    input_data = request.get_json()
    validity = validation.validate_update(input_data)
    if isinstance(validity, bool):
        new_value = check_value(input_data['change_col'],input_data['new_value'])
        where_value = check_value(input_data['where_col'],input_data['where_value'])
        query = f"update student set {input_data['change_col']} = {new_value} where {input_data['where_col']} = {where_value}"
        message = db.update_table(query)
        return jsonify(give_response(data=[], message=message, start_time=start_time))
    else:
        return jsonify(error_handler.generate_error_response(validity))


def delete_operation():
    start_time = datetime.now()
    input_data = {}
    input_data = request.get_json()
    validity = validation.validate_delete(input_data)
    if isinstance(validity, bool):
        where_value = check_value(input_data['where_col'],input_data['where_value'])
        query = f"delete from student where {input_data['where_col']} = {where_value}"
        message = db.delete_from_table(query)
        return jsonify(give_response(data=[], message=message, start_time=start_time))
    else:
        return jsonify(error_handler.generate_error_response(validity))


def student_login():

    start_time = datetime.now()
    input_data = {}
    input_data = request.get_json()
    validity = validation.validate_insert(input_data)

    if isinstance(validity, bool):
        query = f"select password from student where username = '{input_data['username']}'"
        store_password = db.read_from_table(query)

        if give_hash(input_data['password']) == store_password[0][0]:
            return jsonify(give_response(data=[], message="login successful !!", start_time=start_time))
        else:
            return jsonify(give_response(data=[], message="wrong username or password !!", start_time=start_time))
    else:
        return jsonify(error_handler.generate_error_response(validity))


