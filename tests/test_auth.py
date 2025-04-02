from app import db
import json
from models import User
from passlib.hash import pbkdf2_sha256

def test_user_registration(test_client):
    data = {
        "email": "testuser@example.com",
        "password": "TestPassword123",
        "role": "Patient"
    }
    response = test_client.post('/api/auth/register', json=data)
    assert response.status_code == 201
    assert b"User registered successfully" in response.data

def test_user_login(test_client):
    test_email = "testuser@example.com"
    test_password = "TestPassword123"
    
    with test_client.application.app_context():
        # Clean up any existing user
        existing_user = User.query.filter_by(email=test_email).first()
        if existing_user:
            db.session.delete(existing_user)
            db.session.commit()
        
        # Create new test user with passlib's hashing
        user = User(email=test_email,
                   password_hash=pbkdf2_sha256.hash(test_password),
                   role="Patient")
        db.session.add(user)
        db.session.commit()
    
    # Test login
    login_data = {"email": test_email, "password": test_password}
    response = test_client.post('/api/auth/login', json=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json
