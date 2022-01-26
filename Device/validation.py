from cerberus import Validator 

def validation_update(body):
   v = Validator()
   v.schema ={
    'time1':{
        'type':'string',
        'maxlength':8,
        'regex':'^[0-1][0-9]:[0-5][0-9]:[0-5][0-9]$|^[2][0-3]:[0-5][0-9]:[0-5][0-9]'
    },
    'time2':{
        'type':'string',
        'maxlength':8,
        'regex':'^[0-1][0-9]:[0-5][0-9]:[0-5][0-9]$|^[2][0-3]:[0-5][0-9]:[0-5][0-9]'
    },
    'device':{
        'type':'string',
        'maxlength':2,
        'regex':'^D[1-3]$'
    }
}
   val= v.validate(body)
   if val:
      return True
   else:
      return v.errors


def validation_read(body):
   v = Validator()
   v.schema ={
    'device':{
        'type':'string',
        'maxlength':2,
        'regex':'^D[1-3]$'
    }
}
   val= v.validate(body)
   if val:
      return True
   else:
      return v.errors