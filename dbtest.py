import sqlite3
from Login_module.models import User
from flask import Flask, jsonify

app = Flask(__name__)
connection = sqlite3.connect('petshop.db')


# with open('schema.sql') as f:
#     connection.executescript(f.read())

cur = connection.cursor()

# Query for the User table
query_user_table = "SELECT * FROM User;"

# Query for the Product table
query_product_table = "SELECT * FROM Product;"

# Query for the OrderTable table
query_order_table = "SELECT * FROM OrderTable;"

# Query for the Product table
query_product_table = "SELECT * FROM Products;"

# Query for the Order table
query_order_table = "SELECT * FROM Orders;"

# Query for the Review table
query_review_table = "SELECT * FROM Review;"

# Query for the CartItem table
query_cartitem_table = "SELECT * FROM CartItems;"

# Query for the Category table
query_category_table = "SELECT * FROM Categories;"
name = "Kaustav Sarkar"
# q = cur.execute("SELECT * FROM User WHERE name LIKE ?", ('%' + name + '%',))
qq = cur.execute("SELECT * FROM User WHERE id = 20")
# with app.app_context():
#     email = "ale@example.com"
#     user = User.find_by_email(email)
#     print(type(user.created))
#     result = jsonify({'user':user.to_dict()})

#     print(result)
# user_id=2
# q = cur.execute('SELECT role FROM User WHERE id = ?', (user_id,))
# user_role = cur.fetchone()[0]
# print(user_role)
# cur.execute(query_user_table)
print(cur.fetchall())
connection.commit()
connection.close()