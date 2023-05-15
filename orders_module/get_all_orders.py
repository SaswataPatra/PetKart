import sqlite3
from flask import jsonify

def api_func():
    try:
        # Retrieve all orders from the database
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM OrderTable')
        rows = cur.fetchall()
        conn.close()

        # Convert the orders to a list of dictionaries
        orders = []
        for row in rows:
            order = {
                'id': row[0],
                'user_id': row[1],
                'product_id': row[2],
                'quantity': row[3],
                'amount': row[4],
                'status': row[5],
                'created': row[6]
            }
            orders.append(order)

        return jsonify(orders), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
