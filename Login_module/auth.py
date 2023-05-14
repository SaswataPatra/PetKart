from flask import jsonify, request,Blueprint
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity, JWTManager
from .models import User
from datetime import datetime, timedelta

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

@bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    user = User.find_by_email(email)
    print(user.name)
    if user and user.verify_password(password):
        # access_token = create_access_token(identity=user.to_json())
        # Set expiration time for token
        expires_delta = timedelta(minutes=30)
        access_token = create_access_token(identity=user.to_json(), expires_delta=expires_delta)
        # print("access :",access_token)
        return jsonify({'access_token': access_token, 'user': user.to_dict()})
    else:
        return jsonify({'error': 'Invalid email or password'}), 401


