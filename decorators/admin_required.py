from flask import request,jsonify
import sqlite3
from functools import wraps

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # check if the user making the request is an admin
        # you can do this by retrieving the user's role from the database using the user's id or email
        # if the user's role is 'admin', then allow the request to proceed
        # otherwise, return an error response
        user_id = request.headers.get('user_id')
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()
        cur.execute('SELECT role FROM User WHERE id = ?', (user_id,))
        user_role = cur.fetchone()[0]
        if user_role == 'admin':
            return f(*args, **kwargs)
        else:
            return jsonify({'error': 'Unauthorized access'}), 401
    return decorated_function

