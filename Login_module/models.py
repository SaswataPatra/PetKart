from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import sqlite3,json

class User:
    def __init__(self, id, name, email, password, role='customer', billing_address=None,
                 shipping_address=None, payment_methods=None, image=None, created=None):
        self.id = id
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.role = role
        self.billing_address = billing_address
        self.shipping_address = shipping_address
        self.payment_methods = payment_methods
        self.image = image
        self.created = created or datetime.now()

    @staticmethod
    def find_by_email(email):
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM User WHERE email = ?', (email,))
        user_data = cur.fetchone()
        if user_data:
            return User(*user_data)
        return None


    def to_json(self):
        return json.dumps(self.to_dict(), default=self.json_encoder)

    @staticmethod
    def json_encoder(obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        raise TypeError(f'Object of type {type(obj)} is not JSON serializable')
    
    def verify_password(self, password):
        return check_password_hash(self.password, password)
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'role': self.role,
            'billing_address': self.billing_address,
            'shipping_address': self.shipping_address,
            'payment_methods': self.payment_methods,
            'image': self.image,
            'created': str(self.created)
        }