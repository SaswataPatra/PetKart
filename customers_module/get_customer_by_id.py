from flask import jsonify
import sqlite3

def api_func(id):
    try:
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM User WHERE id = ?', (id,))
        row = cur.fetchone()
        if not row:
            return jsonify({'success': False, 'message': 'Customer not found'}), 404
        customer = {
            'id': row[0],
            'name': row[1],
            'email': row[2],
            'billing_address': row[4],
            'shipping_address': row[5],
            'payment_methods': row[6],
            'image': row[7],
            'role': row[8],
            'created': row[9],
        }
        conn.close()
        return jsonify(customer), 200
    except sqlite3.Error as error:
        return jsonify({'success': False, 'message': str(error)}), 500