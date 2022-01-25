from flask import Flask
from Student import route as student_route
from Utilities import error_handler
from Device import route as device_route

app = Flask(__name__)

app.register_blueprint(student_route.student_routes)
app.register_blueprint(error_handler.bp_errors)
app.register_blueprint(device_route.device_routes)

if __name__ == '__main__':
    app.env = 'development'
    app.debug = True
    app.run(host='127.0.0.1',port=8001,debug=True)