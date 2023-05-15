import sqlite3
from flask import jsonify

def api_func(order_id):
    try:
        # Retrieve the order from the database by id
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM OrderTable WHERE id = ?', (order_id,))
        row = cur.fetchone()
        conn.close()

        # Check if the order exists
        if not row:
            return jsonify({'error': 'Order not found.'}), 404

        # Convert the order to a dictionary
        order = {
            'id': row[0],
            'user_id': row[1],
            'product_id': row[2],
            'quantity': row[3],
            'amount': row[4],
            'status': row[5],
            'created': row[6]
        }

        return jsonify(order), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
