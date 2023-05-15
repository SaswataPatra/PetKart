import sqlite3
from flask import jsonify

def add(request):
    try:
        # Retrieve order details from the request
        product_id = request.json.get('product_id')
        quantity = request.json.get('quantity')

        # Perform any necessary validations on the order details
        if not product_id or not quantity:
            return jsonify({'success': False, 'message': 'Product ID and quantity are required'}), 400

        # Retrieve the price of the product from the database
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()
        cur.execute('SELECT price FROM Product WHERE id = ?', (product_id,))
        row = cur.fetchone()
        if not row:
            conn.close()
            return jsonify({'success': False, 'message': 'Product not found'}), 404

        price = row[0]
        amount = price * quantity

        # Insert the order into the database
        cur.execute('INSERT INTO OrderTable (product_id, quantity, amount, status) VALUES (?, ?, ?, ?)',
                    (product_id, quantity, amount, 'pending'))
        order_id = cur.lastrowid

        conn.commit()
        conn.close()

        # Return success message with the order ID
        return jsonify({'success': True, 'order_id': order_id, 'message': 'Order added successfully'}), 200

    except Exception as e:
        # Return error message if there was an exception during order creation
        return jsonify({'success': False, 'message': str(e)}), 500
