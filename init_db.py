import sqlite3

conn = sqlite3.connect('database.db')


with open('schema.sql') as f:
    conn.executescript(f.read())

cur = conn.cursor()

# Insert some dummy data into the User table
cur.execute("INSERT INTO User (name, email, password, billing_address, shipping_address, payment_methods, image) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('John Doe', 'john@example.com', 'password123', '123 Main St', '456 Maple Ave', 'credit card', None))
cur.execute("INSERT INTO User (name, email, password, billing_address, shipping_address, payment_methods, image) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('Jane Smith', 'jane@example.com', 'letmein', '789 Oak Rd', '1010 Pine St', 'paypal', None))

# Insert some dummy data into the Product table
cur.execute("INSERT INTO Product (name, description, price, category, image, stock) VALUES (?, ?, ?, ?, ?, ?)",
            ('Dog Food', 'Premium dog food made from high-quality ingredients', 49.99, 'Pet Food', None, 100))
cur.execute("INSERT INTO Product (name, description, price, category, image, stock) VALUES (?, ?, ?, ?, ?, ?)",
            ('Cat Toy', 'Interactive toy for cats that provides hours of entertainment', 9.99, 'Pet Supplies', None, 50))

# Insert some dummy data into the Order table
cur.execute("INSERT INTO OrderTable (user_id, product_id, quantity, amount, status) VALUES (?, ?, ?, ?, ?)",
            (1, 2, 2, 19.98, 'Processing'))
cur.execute("INSERT INTO OrderTable (user_id, product_id, quantity, amount, status) VALUES (?, ?, ?, ?, ?)",
            (2, 1, 1, 49.99, 'Shipped'))

# Insert some dummy data into the Review table
cur.execute("INSERT INTO Review (user_id, product_id, rating, text) VALUES (?, ?, ?, ?)",
            (1, 2, 4, 'My cat loves this toy!'))
cur.execute("INSERT INTO Review (user_id, product_id, rating, text) VALUES (?, ?, ?, ?)",
            (2, 1, 3, 'My dog is picky about his food, but he seems to like this one.'))


# Insert dummy data into CartItems table
cart_items_data = [
    (1, 1, 2, 3),
    (2, 1, 4, 1),
    (3, 2, 1, 2),
    (4, 3, 3, 4)
]
cur.executemany('INSERT INTO CartItems (id, user_id, product_id, quantity) VALUES (?, ?, ?, ?)', cart_items_data)

# Insert dummy data into Categories table
categories_data = [
    ('Dogs', 'Products for dogs'),
    ('Cats', 'Products for cats'),
    ('Birds', 'Products for birds')
]
cur.executemany('INSERT INTO Categories (name, description) VALUES (?, ?)', categories_data)


# Commit the changes and close the connection
conn.commit()
conn.close()

