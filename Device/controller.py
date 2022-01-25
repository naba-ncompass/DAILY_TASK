from flask import jsonify , request
from Utilities.db import read_peak_consumption_between_times,read_sum_consumption_between_times,read_duplicate_time_between_times
from Device.validation import *
from Utilities.error_handler import validation_err

def create_Result(data,func_name):
    result = {}
    result['isSuccess'] = True
    result['data'] = data
    if(func_name =='get_peak_consumption_between_times'):
        result['message'] = 'Read record' if(data!=None) else "No record"
    elif(func_name =='get_sum_consumption_between_times'):
        result['message'] = 'Read record' if(data!=None) else "No record"
    elif(func_name == 'get_duplicate_time_between_times'):
        result['message'] = 'Read all records' if(data!=None) else "No record/s"
    return result


def get_peak_consumption_between_times():
    params = request.args
    start_time = params['start_time']
    end_time = params['end_time']
    device = params['device']

    if isinstance(check(params),bool) and check(params)==True:
        sql_command = f"SELECT MAX(CONSUMPTION),DEVICE FROM DC where TIME(TIME) > '{start_time}' AND TIME(TIME) < '{end_time}' group by DEVICE having DEVICE = '{device}'"
        data = read_peak_consumption_between_times(sql_command)
        result = create_Result(data,"get_peak_consumption_between_times")
        return jsonify(result)

    return validation_err(check(params))


def get_sum_consumption_between_times():
    params = request.args
    start_time = params['start_time']
    end_time = params['end_time']
    device = params['device']

    if isinstance(check(params),bool) and check(params)==True:
        sql_command = f"SELECT SUM(CONSUMPTION),DEVICE FROM DC where TIME(TIME) > '{start_time}' AND TIME(TIME) < '{end_time}' group by DEVICE having DEVICE = '{device}'"
        data = read_sum_consumption_between_times(sql_command)
        result = create_Result(data,"get_sum_consumption_between_times")
        return jsonify(result)
    
    return validation_err(check(params))

def get_duplicate_time_between_times():
    params = request.args
    start_time = params['start_time']
    end_time = params['end_time']
    device = params['device']

    if isinstance(check(params),bool) and check(params)==True:
        sql_command = f"SELECT DEVICE, TIME, COUNT(TIME) AS COUNT FROM DC where TIME(TIME) > '{start_time}' AND TIME(TIME) < '{end_time}' group by DEVICE, TIME HAVING COUNT(TIME)>1 and DEVICE = '{device}'"
        data = read_duplicate_time_between_times(sql_command)
        result = create_Result(data,"get_duplicate_time_between_times")
        return jsonify(result)

    return validation_err(check(params))

    
    