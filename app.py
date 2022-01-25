from flask import Flask 
from Shows.routes import bp
from Device.routes import d_bp
from Students.routes import s_bp
from Utilities.error_handler import err_bp


app = Flask(__name__)

app.register_blueprint(err_bp)
app.register_blueprint(bp)
app.register_blueprint(d_bp)
app.register_blueprint(s_bp)

if __name__  == "__main__":
    app.env = "development"
    app.run(debug=True)

