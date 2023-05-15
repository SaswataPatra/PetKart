from flask import request,jsonify
import sqlite3
from functools import wraps

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            user_id = request.headers.get('user_id')
            print("user id :- ", user_id)
            conn = sqlite3.connect('petshop.db')
            cur = conn.cursor()
            cur.execute('SELECT role FROM User WHERE id = ?', (user_id,))
            row = cur.fetchone()
            # print("ROLEEEEE",row[0])
            if row is not None and row[0] == 'admin':
                return f(*args, **kwargs)
            else:
                return jsonify({'error': 'Unauthorized access'}), 401
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    return decorated_function

