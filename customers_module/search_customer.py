import sqlite3
from flask import jsonify

def search(request):
    try:
        query_parameters = request.args
        name = query_parameters.get('name')
        email = query_parameters.get('email')
        phone = query_parameters.get('phone')

        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()

        if name:
            cur.execute("SELECT * FROM User WHERE name LIKE ?", ('%' + name + '%',))
        elif email:
            cur.execute("SELECT * FROM User WHERE email LIKE ?", ('%' + email + '%',))
        elif phone:
            cur.execute("SELECT * FROM User WHERE phone LIKE ?", ('%' + phone + '%',))
        else:
            return jsonify({'success': False, 'message': 'No search parameter found'}), 400

        rows = cur.fetchall()
        print(rows)
        customers = []
        for row in rows:
            customer = {
                'id': row[0],
                'name': row[1],
                'email': row[2],
                'phone': row[3],
                'address': row[4],
                'role': row[8],
            }
            customers.append(customer)

        conn.close()
        return jsonify(customers), 200

    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
