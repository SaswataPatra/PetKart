from flask import jsonify
import sqlite3


def api_func():
    try:
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM User WHERE role = "customer"')
        rows = cur.fetchall()
        customers = []
        for row in rows:
            customer = {
                'id': row[0],
                'name': row[1],
                'email': row[2],
                'billing_address': row[4],
                'shipping_address': row[5],
                'payment_methods': row[6],
                'image': row[7],
                'created': row[9]
            }
            customers.append(customer)
        conn.close()
        return jsonify(customers), 200
    except sqlite3.Error as error:
        return jsonify({'success': False, 'message': str(error)}), 500
