from app import db
import json
from models import Doctor

def test_create_doctor(test_client):
    data = {
        "first_name": "Dr. Smith",
        "last_name": "Johnson",
        "email": "drsmith@example.com",
        "phone": "987654321",
        "specialization": "Cardiology"
    }
    response = test_client.post("/api/doctors", json=data, follow_redirects=True)
    assert response.status_code == 201