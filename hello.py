from flask import Flask , escape

"""
#The first argument is the name of the application’s module or package.
#  __name__ is a convenient shortcut for this that is appropriate for most cases. 
"""

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! We are the World!</p>"


@app.route("/<name>")
def hello(name):
    return f"Hello {escape(name)}"


