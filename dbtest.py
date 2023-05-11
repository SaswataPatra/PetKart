import sqlite3

connection = sqlite3.connect('database.db')


# with open('schema.sql') as f:
#     connection.executescript(f.read())

cur = connection.cursor()


# Query for the User table
query_user_table = "SELECT * FROM User;"

# Query for the Product table
query_product_table = "SELECT * FROM Product;"

# Query for the OrderTable table
query_order_table = "SELECT * FROM OrderTable;"

# Query for the User table
query_user_table = "SELECT * FROM Users;"

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



cur.execute(query_category_table)
print(cur.fetchall())
connection.commit()
connection.close()