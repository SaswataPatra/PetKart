-- Create the User table
CREATE TABLE IF NOT EXISTS User (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT UNIQUE,
    password TEXT,
    billing_address TEXT,
    shipping_address TEXT,
    payment_methods TEXT,
    image BLOB,
    role TEXT DEFAULT 'customer',
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Create the Product table
CREATE TABLE IF NOT EXISTS Product (
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT,
    price REAL,
    category TEXT,
    image BLOB,
    stock INTEGER,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
-- Create the Order table
CREATE TABLE IF NOT EXISTS OrderTable(
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    amount REAL,
    status TEXT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES User(id),
    FOREIGN KEY(product_id) REFERENCES Product(id)
);
-- Create the Review table
CREATE TABLE IF NOT EXISTS Review (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    product_id INTEGER,
    rating INTEGER,
    text TEXT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES User(id),
    FOREIGN KEY(product_id) REFERENCES Product(id)
);
CREATE TABLE IF NOT EXISTS CartItems(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(id),
    FOREIGN KEY (product_id) REFERENCES Products(id)
);

CREATE TABLE IF NOT EXISTS Categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
);
