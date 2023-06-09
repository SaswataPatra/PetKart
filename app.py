#decorators imports
from decorators.admin import admin_required
from decorators.staff import staff_required
# from decorators.dummy import dummy_decorator
import sqlite3
from flask import Flask,g,request,jsonify
from flask_cors import CORS
#customer module imports
import customers_module.add_customer as add_customer
import customers_module.get_all_customers as get_all_customers
import customers_module.get_customer_by_id as get_customer_by_id
import customers_module.update_customer as update_customer
import customers_module.search_customer as search_customer
import customers_module.del_cust as delete_customer
#order modules imports
import orders_module.add_order as add_order
import orders_module.get_all_orders as get_all_orders
import orders_module.get_order_by_id as get_order_by_id
import orders_module.update_order as update_order
import orders_module.delete_order as delete_order
#product module imports 
import products_module.add_product as add_product
import products_module.get_all_products as get_all_products
import products_module.get_product_by_id as get_product_by_id
import products_module.update_product as update_product
import products_module.delete_product as delete_product


from flask_jwt_extended import JWTManager,jwt_required,get_jwt
from Login_module.auth import bp as auth_bp
# Register the cart_module Blueprint
from cart_module.routes import cart_module
import time

app = Flask(__name__) 
app.config['JWT_SECRET_KEY'] = 'super-secret'
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(cart_module)
cors = CORS(app, origins='*')


jwt = JWTManager(app)

DATABASE = '/path/to/petshop.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db
"""CUSTOMER API ENDPOINTS"""

# Endpoint to get all customers

@app.route('/', methods=['GET'])
def index():
    return { "status": "OK" }

@app.route('/customers', methods=['GET'])
@jwt_required()
@admin_required
def get_customers_api():
    # Check if token has expired
    if get_jwt()['type'] == 'access' and get_jwt()['exp'] < time.time():
        return jsonify({'error': 'Token has expired'}), 401
    customers, status_code = get_all_customers.api_func()  # call api_func to get customers and status code
    return customers, status_code  # return customers and status code as JSON response
    

# Endpoint to get a single customer by id
@app.route('/customers/<int:id>', methods=['GET'])
def get_customer_api(id):
    customers, status_code = get_customer_by_id.api_func(id)  # call api_func to get customers by id and status code
    return customers, status_code  # return customers and status code as JSON response

# Endpoint to add a new customer
@app.route('/customers', methods=['POST'])
@admin_required
def add_customers():
    success,message = add_customer.add(request)
    if success:
        return jsonify({'success': True, 'message': message}), 200
    else:
        return jsonify({'success': False, 'message': message}), 400

# Endpoint to delete a customer by id
@app.route('/customer/<int:id>', methods=['DELETE'])
@admin_required
def delete_customer_api(id):
    success,message = delete_customer.delete_customer_by_id(id)
    if success:
        return jsonify({'success': True, 'message': message}), 200
    else:
        return jsonify({'success': False, 'message': message}), 400

# Endpoint to update a customer by id
@app.route('/customers/<int:id>', methods=['PUT'])
def update_customer_api(id):
    success, message = update_customer.update(request.json, id)
    if success:
        return jsonify({'success': True, 'message': message}), 200
    else:
        return jsonify({'success': False, 'message': message}), 400

# Endpoint to search for customers by name or email
@app.route('/customers/search', methods=['GET'])
def search_customers_api():
    customers, status_code = search_customer.search(request)
    return customers, status_code

# -----ORDER API ENDPOINTS------


# Endpoint to get all orders
@app.route('/orders', methods=['GET'])
def get_orders_api():
    orders, status_code = get_all_orders.api_func()  # call api_func to get orders and status code
    return orders, status_code  # return orders and status code as JSON response

# Endpoint to get a single order by id
@app.route('/orders/<int:id>', methods=['GET'])
def get_order_api(id):
    order, status_code = get_order_by_id.api_func(id)  # call api_func to get order by id and status code
    return order, status_code  # return order and status code as JSON response

# Endpoint to add a new order
@app.route('/orders', methods=['POST'])
def add_order_api():
    success, message = add_order.add(request)
    if success:
        return jsonify({'success': True, 'message': message}), 200
    else:
        return jsonify({'success': False, 'message': message}), 400

# Endpoint to delete an order by id
@app.route('/orders/<int:id>', methods=['DELETE'])
def delete_order_api(id):
    success, message = delete_order.delete_order_by_id(id)
    if success:
        return jsonify({'success': True, 'message': message}), 200
    else:
        return jsonify({'success': False, 'message': message}), 400

# Endpoint to update an order by id
@app.route('/orders/<int:id>', methods=['PUT'])
def update_order_api(id):
    success, message = update_order.update(request.json, id)
    if success:
        return jsonify({'success': True, 'message': message}), 200
    else:
        return jsonify({'success': False, 'message': message}), 400

#----PRODUCTS MODULE ENDPOINTS-----
# Endpoint to get all products
@app.route('/products', methods=['GET'])
def get_products_api():
    products, status_code = get_all_products.api_func()  # call api_func to get products and status code
    return products, status_code  # return products and status code as JSON response

# Endpoint to get a single product by id
@app.route('/products/<int:id>', methods=['GET'])
def get_product_api(id):
    product, status_code = get_product_by_id.api_func(id)  # call api_func to get product by id and status code
    return product, status_code  # return product and status code as JSON response

# Endpoint to add a new product
@app.route('/products', methods=['POST'])
def add_product_api():
    success, message = add_product.add(request)
    if success:
        return jsonify({'success': True, 'message': message}), 200
    else:
        return jsonify({'success': False, 'message': message}), 400

# Endpoint to delete a product by id
@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product_api(id):
    success, message = delete_product.delete_product_by_id(id)
    if success:
        return jsonify({'success': True, 'message': message}), 200
    else:
        return jsonify({'success': False, 'message': message}), 400

# Endpoint to update a product by id
@app.route('/products/<int:id>', methods=['PUT'])
@staff_required
def update_product_api(id):
    success, message = update_product.update(request.json, id)
    if success:
        return jsonify({'success': True, 'message': message}), 200
    else:
        return jsonify({'success': False, 'message': message}), 400

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run(debug=True)