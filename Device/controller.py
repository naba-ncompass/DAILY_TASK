from flask import request, Response
from Utilities.db import read_peak_consumption,read_sum_consumption,read_duplicate_time
from Device.validation import *
from Utilities.compression import *
from Utilities.error_handler import validation_err
import time

def create_result(data,func_name):
    result = {}
    result['isSuccess'] = True
    result['data'] = data
    if(func_name =='get_peak_consumption'):
        result['message'] = 'Read record' if(data!=None) else "No record"
    elif(func_name =='get_sum_consumption'):
        result['message'] = 'Read record' if(data!=None) else "No record"
    elif(func_name == 'get_duplicate_time'):
        result['message'] = 'Read all records' if(data!=None) else "No record/s"
    return result
    

def create_response(result,start_time,end_time):
    result['start_time_sec'] = start_time
    result['end_time_sec'] = end_time
    result['duration_sec'] = result['end_time_sec'] - result['start_time_sec']
    result['duration_ms'] = int(result['duration_sec']*1000)

    compressed_result = create_compression(result)
    response = Response(compressed_result,
    content_type="application/json"
    )
    response.content_encoding = 'gzip'
    return response


def get_peak_consumption():
    start_time = time.perf_counter()

    params = request.args
    time1 = params['time1']
    time2 = params['time2']
    device = params['device']

    if isinstance(check(params),bool) and check(params)==True:
        sql_query = f"SELECT MAX(CONSUMPTION),DEVICE FROM DC where TIME(TIME) > '{time1}' AND TIME(TIME) < '{time2}' group by DEVICE having DEVICE = '{device}'"
        data = read_peak_consumption(sql_query)
        result = create_result(data,"get_peak_consumption")
        end_time = time.perf_counter()

        response = create_response(result,start_time,end_time)
        return response

    return validation_err(check(params))


def get_sum_consumption():
    start_time = time.perf_counter()

    params = request.args
    time1 = params['time1']
    time2 = params['time2']
    device = params['device']

    if isinstance(check(params),bool) and check(params)==True:
        sql_query = f"SELECT SUM(CONSUMPTION),DEVICE FROM DC where TIME(TIME) > '{time1}' AND TIME(TIME) < '{time2}' group by DEVICE having DEVICE = '{device}'"
        data = read_sum_consumption(sql_query)
        result = create_result(data,"get_sum_consumption")
        end_time = time.perf_counter()

        response = create_response(result,start_time,end_time)
        return response
    
    return validation_err(check(params))

def get_duplicate_time():
    start_time = time.perf_counter()

    params = request.args
    time1 = params['time1']
    time2 = params['time2']
    device = params['device']

    if isinstance(check(params),bool) and check(params)==True:
        sql_query = f"SELECT DEVICE, TIME, COUNT(TIME) AS COUNT FROM DC where TIME(TIME) > '{time1}' AND TIME(TIME) < '{time2}' group by DEVICE, TIME HAVING COUNT(TIME)>1 and DEVICE = '{device}'"
        data = read_duplicate_time(sql_query)
        result = create_result(data,"get_duplicate_time")
        end_time = time.perf_counter()

        response = create_response(result,start_time,end_time)
        print(response)
        return response

    return validation_err(check(params))

    
    