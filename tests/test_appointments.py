from datetime import date, time, datetime
from app import db
from models import Patient, Doctor, DoctorAvailability

def test_create_appointment(test_client):
    with test_client.application.app_context():
        # Create and save a patient
        patient = Patient(first_name="Alice", last_name="Brown", email="alice@example.com", phone="111222333")
        db.session.add(patient)
        db.session.commit()
        patient = Patient.query.first()  # Reload from DB to avoid DetachedInstanceError

        # Create and save a doctor
        doctor = Doctor(first_name="Dr. Mike", last_name="Smith", email="drmike@example.com",
                        phone="444555666", specialization="Dermatology")
        db.session.add(doctor)
        db.session.commit()
        doctor = Doctor.query.first()  # Reload from DB

        # Add doctor's availability
        available_day = date.today().strftime("%A")  # Get today's weekday (e.g., "Monday")
        availability = DoctorAvailability(
            doctor_id=doctor.id,
            day_of_week=available_day,
            start_time=time(9, 0),  # 9:00 AM
            end_time=time(17, 0)    # 5:00 PM
        )
        db.session.add(availability)
        db.session.commit()

        # Create appointment within the doctor's available hours
        data = {
            "patient_id": patient.id,
            "doctor_id": doctor.id,
            "appointment_date": "2025-04-02",  # Convert to string
            "appointment_time": "10:30:00",  # Ensure it's a string
            "status": "Scheduled"
        }
        response = test_client.post("/api/appointments/", json=data)
        print(response.json)

        # Assert the appointment is successfully created
        assert response.status_code == 201, f"Expected 201, got {response.status_code}: {response.json}"