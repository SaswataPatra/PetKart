class CartItem:
    def __init__(self, user_id, product_id, quantity):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity

class Product:
    def __init__(self, name, description, price, category, image, stock):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.image = image
        self.stock = stock

