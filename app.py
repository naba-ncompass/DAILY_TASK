from flask import Flask
import json
from Student import route as student_route
from Utilities import error_handler
from Device import route as device_route

app = Flask(__name__)

app.register_blueprint(student_route.student_routes)
app.register_blueprint(error_handler.bp_errors)
app.register_blueprint(device_route.device_routes)

if __name__ == '__main__':
    with open('config/config.json','r') as c:
        app_config = json.load(c)["app_config"]
    app.env = 'development'
    app.run(host=app_config['host'],port=app_config['port'],debug=True)