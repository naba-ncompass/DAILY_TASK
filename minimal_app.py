from flask import Flask, url_for, render_template
from markupsafe import escape


app = Flask(__name__)

# routing
@app.route("/")
@app.route("/home")
def home():
    return "<h1>Welcome Home Page!</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

# html escape
@app.route("/<name>")
def hello(name):
    return f"<h2> Hello, {name}! </h2>"

# variable rules
@app.route('/user/<username>') # string: text without slash
def show_user_profile(username):
    return f'<h2>User {escape(username)}</h2>'

@app.route('/post/<int:post_id>') # int: positive integers
def show_post(post_id):
    return f'<h2>Post {post_id}</h2>'

@app.route('/path/<path:subpath>') # path: like string with /
def show_subpath(subpath):
    return f'<h2>Subpath {escape(subpath)}</h2>'

@app.route('/path/<float:grade>') # float: float numbers
def show_grade(grade):
    return f'<h2>Grade {grade}</h2>'

#url building
with app.test_request_context():
    print(url_for('home'))
    print(url_for('hello',name='arijeet'))
    print(url_for('show_user_profile',username="Naba Ratan"))
    print(url_for('show_post',post_id=2))
    print(url_for('show_subpath',subpath='/like/arijeet'))
    print(url_for('show_grade',grade=8.5))

# simple render_template
@app.route('/demo')
def show_html():
    return render_template('demo.html')







if __name__ == '__main__':

    #running flask app in terminal with flask run
    #export FLASK_APP=minimal_app
    #export FLASK_ENV=development
    #export FLASK_DEBUG=1
    #flask run

    # print(dir(Flask))
    app.env='development'
    app.run(debug=True)