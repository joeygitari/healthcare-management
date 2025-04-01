from flask import Blueprint, request, jsonify
from models import db, User
from passlib.hash import pbkdf2_sha256
import jwt
from datetime import datetime, timedelta
from config import Config

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        password_hash = pbkdf2_sha256.hash(data['password'])
        new_user = User(email=data['email'], password_hash=password_hash, role=data.get('role', 'Patient'))
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and pbkdf2_sha256.verify(data['password'], user.password_hash):
        payload = {
            'user_id': user.id,
            'role': user.role,
            'exp': datetime.utcnow() + timedelta(hours=1)
        }
        token = jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')
        return jsonify({'access_token': token}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401
