import sqlite3
from flask import jsonify

def delete_customer_by_id(id):
    try:
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()
        cur.execute('DELETE FROM User WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Customer deleted successfully'}), 200
    except sqlite3.Error as error:
        return jsonify({'error': str(error)}), 500