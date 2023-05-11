import sqlite3
# from flask import request, jsonify

def add(request):
    # Get data from request
    try:
        data = request.get_json()
        name = data['name']
        email = data['email']
        password = data['password']
        billing_address = data['billing_address']
        shipping_address = data['shipping_address']
        payment_methods = data['payment_methods']
        # image = data['image']

        # Connect to the database
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()

        # Insert customer into the database
        test = cur.execute('INSERT INTO User (name, email, password, billing_address, shipping_address, payment_methods) VALUES (?, ?, ?, ?, ?, ?)', (name, email, password, billing_address, shipping_address, payment_methods))
        print(test)
        # Commit changes and close connection
        conn.commit()
        return True, None
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])
        conn.rollback()
        return False, e.args[0]
    finally:
        conn.close()

    # return jsonify({'message': 'Customer added successfully'})

