from flask import Flask
from Students.route import students_bp
from Device.route import device_bp
from Utilities.error_handler import err
from Utilities.compression import *


app = Flask(__name__)

app.register_blueprint(err)
app.register_blueprint(students_bp,url_prefix='/records')
app.register_blueprint(device_bp,url_prefix='/device')






if __name__ == '__main__':
    app.env='development'
    app.run(debug=True)