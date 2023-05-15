import sqlite3
from datetime import datetime

class Product:
    def __init__(self, name, description, price, category, image, stock):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.image = image
        self.stock = stock
        self.created = datetime.now()

    def save(self):
        try:
            conn = sqlite3.connect('petshop.db')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Product (name, description, price, category, image, stock, created) "
                "VALUES (?, ?, ?, ?, ?, ?, ?)",
                (self.name, self.description, self.price, self.category, self.image, self.stock, self.created)
            )
            conn.commit()
            conn.close()
            return True, 'Product added successfully'
        except Exception as e:
            return False, str(e)
