from cerberus import Validator

schema = {
    'id':{'type':'string', 'maxlength':4, 'regex':'^S+[0-9]+$'},
    'name':{'type':'string'},
    'department':{'type':'string'},
    'cgpa':{'type':'float', 'min':0, 'max':10},
    'username':{'type':'string','regex':'^[a-z0-9._%-]+@[a-z0-9.-]+\.[a-z]{2,4}$'},
    'password':{'type':'string'}
}

def validate_insert(input_data):
    v = Validator()
    if v.validate(input_data, schema):
        return True
    else: 
        return v.errors


def validate_update(input_data):
    data = {
        input_data['change_col']:input_data['new_value'],
        input_data['where_col']:input_data['where_value']
    }
    v = Validator()
    if v.validate(data, schema):
        return True
    else: 
        return v.errors


def validate_delete(input_data):
    data = {
        input_data['where_col']:input_data['where_value']
    }
    v = Validator()
    if v.validate(data, schema):
        return True
    else: 
        return v.errors


def validate_read(input_data):
    data = {
        "id":input_data
    }
    v = Validator()
    if v.validate(data, schema):
        return True
    else: 
        return v.errors