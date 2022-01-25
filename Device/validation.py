from cerberus import Validator

schema = {
    'time1':{'type':'string', 'maxlength':8, 'regex':'^[0-1][0-9]:[0-5][0-9]:[0-5][0-9]$|^[2][0-3]:[0-5][0-9]:[0-5][0-9]'},
    'time2':{'type':'string', 'maxlength':8, 'regex':'^[0-1][0-9]:[0-5][0-9]:[0-5][0-9]$|^[2][0-3]:[0-5][0-9]:[0-5][0-9]'},
    'device':{'type':'string', 'maxlength':2, 'regex':'^D[1-3]$'}
}

def validate_device(input_data):
    v = Validator()
    if v.validate(input_data, schema):
        return True
    else: 
        return v.errors
