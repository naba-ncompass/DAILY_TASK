from cerberus import Validator

v = Validator()


def parse_err(errors):
    message = ''
    for errs in errors:
        message = message + '%s %s , ' % (errs, v.errors[errs][0])
    return message


def validate_time(body):
    schema = {
        'device': {
            'type': 'string',
            'maxlength': 4
        },
        'from': {
            'type': 'string',
            'regex': '^[0-1][0-9]:[0-5][0-9]:[0-5][0-9]$|^[2][0-3]:[0-5][0-9]:[0-5][0-9]'
        },
        'to': {
            'type': 'string',
            'regex': '^[0-1][0-9]:[0-5][0-9]:[0-5][0-9]$|^[2][0-3]:[0-5][0-9]:[0-5][0-9]'
        }
    }

    if v.validate(body, schema):
        return True
    else:
        return {
            "err_code": "Validation Error",
            "message": parse_err(v.errors)
        }


def validate_device(body):
    schema = {
        'device': {
            'type': 'string',
            'maxlength': 4
        }
    }

    if v.validate(body, schema):
        return True
    else:
        return {
            "err_code": "Validation Error",
            "message": parse_err(v.errors)
        }
