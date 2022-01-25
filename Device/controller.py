from flask import jsonify,request
from datetime import datetime
from Utilities import db,error_handler,compression
from Device import validation


def read_from_device():
    start_time = datetime.now()
    params = request.args
    validity = validation.validate_device(params)
    if isinstance(validity, bool):
        query = f"select * from uc3 where device = '{params['device']}'"
        output = db.read_from_table(query)
        
        response = error_handler.give_response(data=output, message='operation successful', start_time=start_time)
        compressed_response = compression.make_compress(response)
        return compressed_response
    
    else:
        return jsonify(error_handler.generate_error_response(validity))


def peak_between_times():
    start_time = datetime.now()
    params = request.get_json()
    validity = validation.validate_device(params)
    if isinstance(validity, bool):
        query = f"select max(CONSUMPTION), DEVICE FROM uc3 where TIME(TIME) > '{params['time1']}' AND TIME(TIME) < '{params['time2']}' group by DEVICE having DEVICE = '{params['device']}'"
        output = db.read_from_table(query)
        return jsonify(error_handler.give_response(data=output, message='operation successful', start_time=start_time))
    else:
        return jsonify(error_handler.generate_error_response(validity))


def sum_between_times():
    params = request.args
    start_time = datetime.now()
    validity = validation.validate_device(params)
    if isinstance(validity, bool):
        query = f"select sum(CONSUMPTION), DEVICE FROM uc3 where TIME(TIME) > '{params['time1']}' AND TIME(TIME) < '{params['time2']}' group by DEVICE having DEVICE = '{params['device']}'"
        output = db.read_from_table(query)
        return jsonify(error_handler.give_response(data=output, message='operation successful', start_time=start_time))
    else:
        return jsonify(error_handler.generate_error_response(validity))


def duplicate_between_times():
    params = request.args
    start_time = datetime.now()
    validity = validation.validate_device(params)
    if isinstance(validity, bool):
        query = f"select DEVICE, TIME, COUNT(TIME), CONSUMPTION FROM uc3 where TIME(TIME) > '{params['time1']}' AND TIME(TIME) < '{params['time2']}' group by DEVICE, TIME HAVING COUNT(TIME)>1 and DEVICE = '{params['device']}'"
        output = db.read_from_table(query)
        return jsonify(error_handler.give_response(data=output, message='operation successful', start_time=start_time))
    else:
        return jsonify(error_handler.generate_error_response(validity))



