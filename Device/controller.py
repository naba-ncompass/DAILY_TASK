from flask import request
from Utilities.db_operations import *
from Utilities.error_handler import custom_response_maker
from .validation import *
from .compression import compress_json

def get_sum_consumption():
    req_params = request.args
    if (isinstance(validate_time(req_params), dict)):
        return custom_response_maker(validate_time(req_params))
    query = "SELECT device ,SUM(consumption)  FROM Device WHERE device='%s' AND time(time) BETWEEN '%s' AND '%s' GROUP BY device;" % (
        req_params['device'], req_params['from'], req_params['to'])
    return compress_json(device_operation(query))


def get_peak_consumption():
    req_params = request.args
    if (isinstance(validate_time(req_params), dict)):
        return custom_response_maker(validate_time(req_params))
    query = "SELECT device ,MAX(consumption)  FROM Device WHERE device='%s' AND time(time) BETWEEN '%s' AND '%s' GROUP BY device;" % (
        req_params['device'], req_params['from'], req_params['to']
    )
    return compress_json(device_operation(query))


def get_duplicate_time():
    req_params = request.args
    if (isinstance(validate_device(req_params), dict)):
        return custom_response_maker(validate_device(req_params))
    query = "SELECT time, COUNT(*) AS count FROM Device WHERE device='%s' GROUP BY time HAVING COUNT(*) > 1;" % (
        req_params['device'])
    return compress_json(device_operation(query))
