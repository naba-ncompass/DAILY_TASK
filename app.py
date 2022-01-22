from flask import Flask, g, Response
from Students.route import app_bp
from Utilities.error_handler import err
import time,json

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Welcome Home Page!</h1>"

app.register_blueprint(err)
app.register_blueprint(app_bp,url_prefix='/records')


@app.before_request
def before_request_func():
    g.start_time = time.perf_counter()

@app.after_request
def after_request_func(response):
    result = dict(response.json)
    result['start_time_sec'] = g.start_time
    result['end_time_sec'] = time.perf_counter()
    result['duration_sec'] = result['end_time_sec'] - result['start_time_sec']
    result['duration_ms'] = int(result['duration_sec']*1000)
    return Response(json.dumps(result)
    ,content_type="application/json")






    
if __name__ == '__main__':
    app.env='development'
    app.run(debug=True)