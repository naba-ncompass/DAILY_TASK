from cerberus import Validator

def check(document):
    schema = {
        'start_time':{
            'type':'string',
            'maxlength':8,
            'regex':'^[0-1][0-9]:[0-5][0-9]:[0-5][0-9]$|^[2][0-3]:[0-5][0-9]:[0-5][0-9]'
        },
        'end_time':{
            'type':'string',
            'maxlength':8,
            'regex':'^[0-1][0-9]:[0-5][0-9]:[0-5][0-9]$|^[2][0-3]:[0-5][0-9]:[0-5][0-9]'
        },
        'device':{
            'type':'string',
            'maxlength':2,
            'regex':'^D[1-3]$'}
    }
    v = Validator(schema)
    if v.validate(document):
        return True
    else:
        return v.errors
