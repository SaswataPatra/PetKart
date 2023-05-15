import sqlite3
from flask import jsonify

def update_order(order_data, order_id):
    try:
        # Check if the order exists
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM OrderTable WHERE id = ?', (order_id,))
        row = cur.fetchone()
        if not row:
            conn.close()
            return jsonify({'success': False, 'message': 'Order not found'}), 400

        # Update the order in the database
        cur.execute('UPDATE OrderTable SET quantity = ?, amount = ?, status = ? WHERE id = ?',
                    (order_data.get('quantity'), order_data.get('amount'), order_data.get('status'), order_id))
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Order updated successfully'}), 200
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
