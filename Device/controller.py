from timeit import default_timer as timer
from datetime import datetime,timedelta
from Device import validation
from Utilities import db
from flask import Flask,jsonify,request,Blueprint
from Utilities import compression

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

def reads_device():
    params = request.args
    start_time = datetime.now()
    
    valid=validation.validation_read(params)
    print("HELLO WORLD")
    if isinstance(valid,bool):
        query = f"select * from uc3 where DEVICE = '{params['device']}'"
        var = db.read(query)
        jsonify(give_response(data=var, message='operation successful', start_time=start_time))
        compressed_response = compression.make_compress(var)
        return compressed_response    
    else:
        return jsonify({ "message" : valid })


def sum_device():
    params = request.args
    start_time = datetime.now()
    
    valid=validation.validation_update(params)
    if isinstance(valid,bool):
        query = f"select max(CONSUMPTION), DEVICE FROM uc3 where TIME(TIME) > '{params['time1']}' AND TIME(TIME) < '{params['time2']}' group by DEVICE having DEVICE = '{params['device']}'"
        var = db.read(query)
        jsonify(give_response(data=var, message='operation successful', start_time=start_time))
        compressed_response = compression.make_compress(var)
        return compressed_response
    else:
        return jsonify({ "message" : valid })
    
def peak_device():
    params = request.args
    start_time = datetime.now()
    valid=validation.validation_update(params)
    if isinstance(valid,bool):
        query = f"select sum(CONSUMPTION), DEVICE FROM uc3 where TIME(TIME) > '{params['time1']}' AND TIME(TIME) < '{params['time2']}' group by DEVICE having DEVICE = '{params['device']}'"
        var = db.read(query)
        jsonify(give_response(data=var, message='operation successful', start_time=start_time))
        compressed_response = compression.make_compress(var)
        return compressed_response
    else:
        return jsonify({ "message" : valid })


def duplicate_device():
    params = request.args
    start_time = datetime.now()
    valid=validation.validation_update(params)
    if isinstance(valid,bool):
        query = f"select DEVICE, TIME, COUNT(TIME), CONSUMPTION FROM uc3 where TIME(TIME) > '{params['time1']}' AND TIME(TIME) < '{params['time2']}' group by DEVICE, TIME HAVING COUNT(TIME)>1 and DEVICE = '{params['device']}'"       
        var = db.read(query)
        jsonify(give_response(data=var, message='operation successful', start_time=start_time))
        compressed_response = compression.make_compress(var)
        return compressed_response
    else:
        return jsonify({ "message" : valid })