from flask import Flask,jsonify,request
from Student import route
import json
from Utilities import db,error_handler
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

app.register_blueprint(route.bp_routes)
app.register_blueprint(error_handler.bp_errors)

# @app.errorhandler(HTTPException)
# def handle_exception(e):
#     response = e.get_response()

#     response.data = json.dumps({
#         "code": e.code,
#         "name": e.name,
#         "description": e.description,
#     })
#     response.content_type = "application/json"
#     return response


if __name__ == '__main__':
    app.env = 'development'
    app.debug = True
    app.run()