from decorators.admin import admin_required
# from decorators.dummy import dummy_decorator
import sqlite3,json,datetime
from flask import Flask, render_template,g,request,jsonify
import customers_module.add_customer as add_customer
import customers_module.get_all_customers as get_all_customers
import customers_module.get_customer_by_id as get_customer_by_id
import customers_module.update_customer as update_customer
import customers_module.search_customer as search_customer
import customers_module.del_cust as delete_customer
app = Flask(__name__)    

DATABASE = '/path/to/petshop.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db
"""CUSTOMER API ENDPOINTS"""

# Endpoint to get all customers
@app.route('/customers', methods=['GET'])
def get_customers_api():
    customers, status_code = get_all_customers.api_func()  # call api_func to get customers and status code
    return customers, status_code  # return customers and status code as JSON response
    

# Endpoint to get a single customer by id
@app.route('/customers/<int:id>', methods=['GET'])
def get_customer_api(id):
    customers, status_code = get_customer_by_id.api_func(id)  # call api_func to get customers by id and status code
    return customers, status_code  # return customers and status code as JSON response

# Endpoint to add a new customer
@app.route('/customers', methods=['POST'])
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

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run(debug=True)