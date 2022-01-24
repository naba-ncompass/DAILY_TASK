from cerberus import Validator


def checkfirstLetter_upper(field,value,error):
    if value[0].islower():
        error(field,"First character must be an upperCase")


def check_get(document):
    schema = {
        'id':{'type':'string','regex':'[0-9]+'},
    }
    v = Validator(schema)
    if v.validate(document):
        return True
    else:
        return v.errors

def check_post(document):
    schema = {
        'id': {'type':'integer'},
        'name':{'type':'string','check_with':checkfirstLetter_upper,'maxlength':30,'minlength':2},
        'dept':{'type':'string','check_with':checkfirstLetter_upper,'maxlength':20,'minlength':2}
    }
    v = Validator(schema)
    if v.validate(document):
        return True
    else:
        return v.errors

def check_patch(document):
    schema = {
        'id': {'type':'string','regex':'[0-9]+'},
        'name':{'type':'string','check_with':checkfirstLetter_upper,'maxlength':30,'minlength':2},
        'dept':{'type':'string','check_with':checkfirstLetter_upper,'maxlength':20,'minlength':2}
    }
    v = Validator(schema)
    if v.validate(document):
        return True
    else:
        return v.errors

def check_delete(document):
    schema = {
        'id':{'type':'string','regex':'[0-9]+'},
    }
    v = Validator(schema)
    if v.validate(document):
        return True
    else:
        return v.errors
