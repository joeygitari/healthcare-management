from app import db
import json
from models import Patient

def test_register_patient(test_client):
    data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@example.com",
        "phone": "123456789",
        "gender": "Male",
        "date_of_birth": "1990-05-05",
        "insurance_provider": "ABC Health",
        "insurance_number": "INS123456"
    }
    response = test_client.post("/api/patients", json=data, follow_redirects=True)
    print(response.json)
    assert response.status_code == 201