import os

from flask import Flask, send_file, abort
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
@app.route("/index/")
def index():
    return send_file('src/index.html')

@app.route("/about/")
def about():
    return '<h3>This is a Flask Web Application</h3>'

@app.route("/capitalize/<word>/")
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))

@app.route("/add/<int:n1>/<int:n2>/")
def add(n1, n2):
    return '<h1>{}</h1>'.format(n1 + n2)

@app.route("/users/<int:user_id>/")
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    try:
        return '<h1>Hi {}</h1>'.format(users[user_id])
    except IndexError:
        abort(404)

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
