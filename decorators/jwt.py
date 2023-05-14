import jwt
import datetime
import sqlite3

# Define the payload for the token
def generate_token(user_id):
    conn = sqlite3.connect('petshop.db')
    cur = conn.cursor()
    cur.execute('SELECT id, role FROM User WHERE id = ?', (user_id,))
    user_data = cur.fetchone()
    if user_data is None:
        return None
    user_id, user_role = user_data

    payload = {
        'sub': user_id,
        'role': user_role,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }

    # Generate the token
    token = jwt.encode(payload, 'secret_key', algorithm='HS256')
    return token
