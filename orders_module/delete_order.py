import sqlite3
from flask import jsonify

def delete_order_by_id(order_id):
    try:
        # Check if the order exists
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM OrderTable WHERE id = ?', (order_id,))
        row = cur.fetchone()
        if not row:
            conn.close()
            return jsonify({'success': False, 'message': 'Order not found'}), 400

        # Delete the order from the database
        cur.execute('DELETE FROM OrderTable WHERE id = ?', (order_id,))
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Order deleted successfully'}), 200
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
