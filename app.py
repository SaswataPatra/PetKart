import sqlite3
from flask import Flask, render_template,g,request,jsonify
import customers_module.add_customer as add_customer
import customers_module.delete_customers as delete_customer
app = Flask(__name__)
from decorators import admin_required

@app.route('/customer/<int:id>', methods=['DELETE'])
@admin_required
def delete_customer_api(id):
    success,message = delete_customer.delete_customer_by_id(id)
    if success:
        return jsonify({'success': True, 'message': message}), 200
    else:
        return jsonify({'success': False, 'message': message}), 400
    

DATABASE = '/path/to/petshop.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.route('/customers', methods=['POST'])
def add_customers():
    success,message = add_customer.add(request)
    if success:
        return jsonify({'success': True, 'message': message}), 200
    else:
        return jsonify({'success': False, 'message': message}), 400
    
@app.route('/customer/<int:id>', methods=['DELETE'])
@admin_required
def delete_customer_by_id(id):
    try:
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()
        cur.execute('DELETE FROM User WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Customer deleted successfully'}), 200
    except sqlite3.Error as error:
        return jsonify({'error': str(error)}), 500

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run(debug=True)