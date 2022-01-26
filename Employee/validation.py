from pickle import TRUE
from cerberus import Validator

def validation_insert(body):
   v = Validator()
   v.schema = {
         'id': { 
            'type': 'integer',
            'minlength': 1
                     },
         'first_name': { 
            'type': 'string',
            'minlength': 2
                     },
         'last_name': { 
            'type': 'string',
            'minlength': 2
                     },
         "email": {
            "type": "string",
            "minlength": 8,
            "maxlength": 255,
            "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
                  },
         'gender': {
            'type': 'string',
                   },
         "phone": {
            "type": "string",
            "minlength": 10,
            "maxlength": 11,
            "regex": "^0[0-9]{9}$"
                  },
         "password": {
            "type": "string",
            "minlength": 8,
            "maxlength": 50
                  }
            }
   
   val= v.validate(body)
   if val:
      return True
   else:
      return v.errors


def validation_update(body):
   v = Validator()
   v.schema = {
         'id': { 
            'type': 'integer',
            'minlength': 1
                     },
         'first_name': { 
            'type': 'string',
            'minlength': 2
                     }
                  
            } 
   val= v.validate(body)
   if val:
      return True
   else:
      return v.errors


def validation_insert_id(body):
   v = Validator()
   v.schema = {
         'id': { 
            'type': 'string',
            'minlength': 1,
            "regex": "[0-9]+"
                     }                  
            } 
   val= v.validate(body)
   if val:
      return True
   else:
      return v.errors


def validation_delete(body):
   v = Validator()
   v.schema = {
         'id': { 
            'type': 'string',
            'minlength': 1,
            "regex": "[0-9]+"
                     }                  
            } 
   val= v.validate(body)
   if val:
      return True
   else:
      return v.errors

def validation_check(body):
   v = Validator()
   v.schema = {
         "email": {
            "type": "string",
            "minlength": 8,
            "maxlength": 255,
            "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
                  },
         "password": {
            "type": "string",
            "minlength": 8,
            "maxlength": 50
                  }
   }
   val= v.validate(body)
   if val:
      return True
   else:
      return v.errors
