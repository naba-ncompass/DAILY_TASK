from crypt import methods
from urllib import response
from flask import Flask 

app = Flask(__name__)

from Shows.routes import bp
app.register_blueprint(bp)

if __name__  == "__main__":
    app.env = "development"
    app.run(debug=True)

