from cerberus import Validator

v = Validator()

def parse_err(errors):
    message = ''
    for errs in errors:
        message = message + '%s %s , ' % (errs, v.errors[errs][0])
    return message

def validate_insert(body):
    schema = {
        'id': {'type': 'integer'},
        'name': {'type': 'string','maxlength': 25},
        'studio': {'type': 'string','maxlength': 25}
    }

    if v.validate(body, schema):
        return True
    else:
        return {
            "err_code": "Validation Error",
            "message": parse_err(v.errors)
        }


def validate_update(body):
    schema = {
        'column': {'type': 'string', 'maxlength': 10},
        'new_value': {'type': 'string', 'maxlength' : 25},
        'id': {'type': 'integer'}
    }

    if v.validate(body, schema):
        return True
    else:
        return {
            "err_code": "Validation Error",
            "message": parse_err(v.errors)
        }


def validate_delete(body):
    schema = {
        'id': {'type': 'integer'},
    }

    if v.validate(body, schema):
        return True
    else:
        return {
            "err_code": "Validation Error",
            "message": parse_err(v.errors)
        }
