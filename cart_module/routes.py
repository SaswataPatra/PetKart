from flask import Blueprint, jsonify, request
# from models import CartItem
import sqlite3
cart_module = Blueprint('cart_module', __name__)


@cart_module.route('/cart', methods=['POST'])
def add_to_cart():
    try:
        # Retrieve data from the request body
        data = request.get_json()
        user_id = data.get('user_id')
        product_id = data.get('product_id')
        quantity = data.get('quantity')

        # Create a new cart item
        # cart_item = CartItem(user_id=user_id, product_id=product_id, quantity=quantity)

        # Insert cart item data into the database
        try:
            conn = sqlite3.connect('petshop.db')
            cur = conn.cursor()
            cur.execute('INSERT INTO CartItems (user_id, product_id, quantity) VALUES (?, ?, ?)',
                        (user_id, product_id, quantity))
            conn.commit()
            conn.close()
            return jsonify({'success': True, 'message': 'Item added to cart successfully'}), 200
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)}), 500
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500


@cart_module.route('/cart/<int:id>', methods=['DELETE'])
def remove_from_cart(id):
    try:
        # Find the cart item by its ID
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM CartItems WHERE id = ?', (id,))
        cart_item = cur.fetchone()
        conn.close()

        if cart_item:
            # Remove the cart item from the database
            conn = sqlite3.connect('petshop.db')
            cur = conn.cursor()
            cur.execute('DELETE FROM CartItems WHERE id = ?', (id,))
            conn.commit()
            conn.close()

            return jsonify({'success': True, 'message': 'Item removed from cart successfully'}), 200
        else:
            return jsonify({'success': False, 'message': 'Cart item not found'}), 404
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500


@cart_module.route('/cart/<int:id>', methods=['PUT'])
def update_cart_item(id):
    try:
        # Retrieve data from the request body
        data = request.get_json()
        quantity = data.get('quantity')

        # Find the cart item by its ID
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM CartItems WHERE id = ?', (id,))
        cart_item = cur.fetchone()
        conn.close()

        if cart_item:
            # Update the quantity of the cart item
            conn = sqlite3.connect('petshop.db')
            cur = conn.cursor()
            cur.execute('UPDATE CartItems SET quantity = ? WHERE id = ?', (quantity, id))
            conn.commit()
            conn.close()

            return jsonify({'success': True, 'message': 'Cart item updated successfully'}), 200
        else:
            return jsonify({'success': False, 'message': 'Cart item not found'}), 404
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500


@cart_module.route('/cart', methods=['GET'])
def get_cart_items():
    try:
        # Fetch all cart items from the database
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM CartItems')
        cart_items = cur.fetchall()
        conn.close()

        # Process the fetched cart items
        items = []
        for item in cart_items:
            item_data = {
                'id': item[0],
                'user_id': item[1],
                'product_id': item[2],
                'quantity': item[3]
            }
            items.append(item_data)

        return jsonify({'success': True, 'cart_items': items}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500