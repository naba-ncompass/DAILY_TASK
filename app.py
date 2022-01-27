from flask import Flask 
from Shows.routes import bp
from Device.routes import d_bp
from Students.routes import s_bp
from Utilities.error_handler import err_bp
import json

from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "super-secret" 
jwt = JWTManager(app)

app.register_blueprint(err_bp)
app.register_blueprint(bp)
app.register_blueprint(d_bp)
app.register_blueprint(s_bp)


with open('Config/config.json') as f:
    config = json.load(f)
    app_config = config["APP_CONFIG"]

if __name__  == "__main__":
    app.env = "development"
    app.run(port=app_config["APP_PORT"],debug=True)

