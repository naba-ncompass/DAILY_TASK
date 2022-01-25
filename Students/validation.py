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
        'username': {'type': 'string','maxlength': 25},
        'email': {
            'type': 'string',
            'maxlength': 25,
            'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$' },
        'password': { 'type': 'string', 'maxlength': 50}
    }

    if v.validate(body, schema):
        return True
    else:
        return {
            "err_code": "Validation Error",
            "message": parse_err(v.errors)
        }


def validate_login(body):
    schema = {
        'username': {
            'type': 'string',
            'maxlength': 25
        },
        'password': { 'type': 'string', 'maxlength': 50}
    }

    if v.validate(body, schema):
        return True
    else:
        return {
            "err_code": "Validation Error",
            "message": parse_err(v.errors)
        }

