# products_module/get_all_products.py

import sqlite3
from flask import jsonify

def api_func():
    try:
        # Connect to the database
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()

        # Retrieve all products from the Product table
        cursor.execute("SELECT * FROM Product")
        products = cursor.fetchall()

        # Format the products as a list of dictionaries
        formatted_products = []
        for product in products:
            formatted_product = {
                'id': product[0],
                'name': product[1],
                'description': product[2],
                'price': product[3],
                'category': product[4],
                'image': product[5],
                'stock': product[6],
                'created': product[7]
            }
            formatted_products.append(formatted_product)

        # Close the database connection
        conn.close()

        # Return the formatted products and the success status code
        return jsonify({'products': formatted_products}), 200

    except Exception as e:
        # Return an error message and the error status code
        return jsonify({'error': str(e)}), 500
