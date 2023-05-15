import sqlite3
from flask import jsonify

def delete_product_by_id(product_id):
    try:
        # Connect to the database
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()

        # Check if the product exists
        cursor.execute("SELECT * FROM Product WHERE id=?", (product_id,))
        product = cursor.fetchone()
        if product is None:
            conn.close()
            return False, 'Product not found'

        # Delete the product
        cursor.execute("DELETE FROM Product WHERE id=?", (product_id,))
        conn.commit()
        conn.close()

        return True, 'Product deleted successfully'

    except Exception as e:
        return False, str(e)
