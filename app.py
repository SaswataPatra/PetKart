# from markupsafe import escape

# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def home():
#      name = "saswata"
#      return f"Hello, {name}"

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'User {escape(username)}'

import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

import sqlite3
from flask import g


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

DATABASE = '/path/to/database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()