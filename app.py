from flask import Flask 
from Shows.routes import bp
from Utilities.error_handler import err_bp


app = Flask(__name__)

app.register_blueprint(err_bp)
app.register_blueprint(bp)

if __name__  == "__main__":
    app.env = "development"
    app.run(debug=True)

