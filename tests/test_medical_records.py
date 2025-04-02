from app import db
import json
from datetime import date, time, datetime
from models import Patient, Doctor, MedicalRecord, Appointment

def test_add_medical_record(test_client):
    with test_client.application.app_context():
        patient = Patient(first_name="John", last_name="Doe", email="john@example.com", phone="123456789")
        doctor = Doctor(first_name="Dr. Jane", last_name="Smith", email="drjane@example.com", phone="555666777", specialization="General")

        db.session.add_all([patient, doctor])
        db.session.commit()

        patient = Patient.query.first()
        doctor = Doctor.query.first()

        # Create an appointment first
        appointment = Appointment(
            patient_id=patient.id,
            doctor_id=doctor.id,
            appointment_date=date.today(),
            appointment_time=time(10, 0),
            status="Completed"
        )
        db.session.add(appointment)
        db.session.commit()
        appointment = Appointment.query.first()

        data = {
            "patient_id": patient.id,
            "appointment_id": appointment.id,  # Add the missing appointment_id
            "diagnosis": "Mild flu",
            "prescription": "Rest, hydration, and paracetamol",
            "notes": "Follow up in a week if symptoms persist"
        }
        response = test_client.post("/api/medical_records", json=data, follow_redirects=True)
        print(response.json)

        assert response.status_code == 201, f"Expected 201, got {response.status_code}: {response.json}"
