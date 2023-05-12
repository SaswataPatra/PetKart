import sqlite3
# from flask import jsonify, request

def update(req,id):
    try:
        
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()

        # Get existing customer by id
        cur.execute('SELECT * FROM User WHERE id = ?', (id,))
        row = cur.fetchone()

        # If customer not found, return error
        if not row:
            conn.close()
            return False, 'Customer not found'

        # Extract data from request body
        data = req
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        billing_address = data.get('billing_address')
        shipping_address = data.get('shipping_address')
        payment_methods = data.get('payment_methods')
        image = data.get('image')
        role = data.get('role')

        # Update customer fields if provided in request body
        if name:
            cur.execute('UPDATE User SET name = ? WHERE id = ?', (name, id))
        if email:
            cur.execute('UPDATE User SET email = ? WHERE id = ?', (email, id))
        if password:
            cur.execute('UPDATE User SET password = ? WHERE id = ?', (password, id))
        if billing_address:
            cur.execute('UPDATE User SET billing_address = ? WHERE id = ?', (billing_address, id))
        if shipping_address:
            cur.execute('UPDATE User SET shipping_address = ? WHERE id = ?', (shipping_address, id))
        if payment_methods:
            cur.execute('UPDATE User SET payment_methods = ? WHERE id = ?', (payment_methods, id))
        if image:
            cur.execute('UPDATE User SET image = ? WHERE id = ?', (image, id))
        if role:
            cur.execute('UPDATE User SET role = ? WHERE id = ?', (role, id))

        # Commit changes to database
        conn.commit()
        conn.close()

        return True, 'Customer updated successfully'
    
    except sqlite3.Error as error:
        return False, str(error)
