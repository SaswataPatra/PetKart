from decorators.admin import admin_required

from flask import jsonify, request,Blueprint
from flask_jwt_extended import jwt_required, create_access_token, get_jwt, JWTManager
from .models import User
from datetime import datetime, timedelta
import re


bp = Blueprint('auth', __name__)
jwt = JWTManager()

@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return jsonify({'error': 'Unauthorized access'}), 401

@jwt.expired_token_loader
def expired_token_callback(expired_token):
    return jsonify({'error': 'Token has expired'}), 401

@jwt.invalid_token_loader
def invalid_token_callback(invalid_token):
    return jsonify({'error': 'Invalid token'}), 401

from flask import request, jsonify
import sqlite3
from werkzeug.security import generate_password_hash

@bp.route('/signup', methods=['POST'])
def signup():
    # Retrieve user input from request body
    name = request.json.get('name')
    email = request.json.get('email')
    password = request.json.get('password')
    billing_address = request.json.get('billing_address')
    shipping_address = request.json.get('shipping_address')
    payment_methods = request.json.get('payment_methods')
    image = request.json.get('image')

    # Hash user's password for security
    hashed_password = generate_password_hash(password)


    # Validate user input
    if not name or not email or not password:
        return jsonify({'error': 'Name, email, and password are required.'}), 400
    
    # Check if email is valid
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        return jsonify({'error': 'Invalid email format.'}), 400

    # Check if user already exists
    if User.find_by_email(email):
        return jsonify({'error': 'User with that email already exists.'}), 409


    # Insert user data into database
    try:
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()
        cur.execute('INSERT INTO User (name, email, password, billing_address, shipping_address, payment_methods, image) VALUES (?, ?, ?, ?, ?, ?, ?)',
                    (name, email, hashed_password, billing_address, shipping_address, payment_methods, image))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Account created successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

# Enroll admin route
@bp.route('/admin/enroll', methods=['POST'])
@jwt_required()
@admin_required
def enroll_admin():
    try:
        # Retrieve user input from request body
        name = request.json.get('name')
        email = request.json.get('email')
        password = request.json.get('password')
        billing_address = request.json.get('billing_address')
        shipping_address = request.json.get('shipping_address')
        payment_methods = request.json.get('payment_methods')
        image = request.json.get('image')

        # Hash user's password for security
        hashed_password = generate_password_hash(password)

        # Validate user input
        if not name or not email or not password:
            return jsonify({'error': 'Name, email, and password are required.'}), 400

        # Check if email is valid
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            return jsonify({'error': 'Invalid email format.'}), 400

        # Check if user already exists
        if User.find_by_email(email):
            return jsonify({'error': 'User with that email already exists.'}), 409

        try:
            conn = sqlite3.connect('petshop.db')
            cur = conn.cursor()
            cur.execute('INSERT INTO User (name, email, password, billing_address, shipping_address, payment_methods, image, role) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                        (name, email, hashed_password, billing_address, shipping_address, payment_methods, image, 'admin'))
            conn.commit()
            conn.close()
            return jsonify({'message': 'Admin enrolled successfully!'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/login', methods=['POST'])
def login():
    try:
        email = request.json.get('email')
        password = request.json.get('password')
        user = User.find_by_email(email)
        print(user.name)
        if user and user.verify_password(password):
            # Set expiration time for token
            expires_delta = timedelta(minutes=30)
            access_token = create_access_token(identity=user.to_json(), expires_delta=expires_delta)
            return jsonify({'access_token': access_token, 'user': user.to_dict()})
        else:
            return jsonify({'error': 'Invalid email or password'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# @bp.route('/logout', methods=['DELETE'])
# @jwt_required()
# def logout():
#     try:
#         jti = get_jwt()['jti']  # Get the unique identifier for the JWT
#         JWTManager._set_in_blacklist(jti=jti, expires=0)  # Set token to be invalid immediately
#         return jsonify({"message": "Successfully logged out"}), 200
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500


