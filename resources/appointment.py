from flask import Blueprint, request, jsonify
from models import db, Appointment, DoctorAvailability, Doctor
from datetime import datetime

appointment_bp = Blueprint('appointment_bp', __name__)

@appointment_bp.route('/', methods=['POST'])
def create_appointment():
    try:
        data = request.get_json()
        data['appointment_date'] = datetime.strptime(data["appointment_date"], "%Y-%m-%d").date()
        patient_id = data['patient_id']
        doctor_id = data['doctor_id']
        appointment_date = data['appointment_date']
        appointment_time = data['appointment_time']

        # Verify doctor exists and availability
        doctor = Doctor.query.get_or_404(doctor_id)
        day_of_week = appointment_date.strftime('%A')
        
        availability = DoctorAvailability.query.filter_by(doctor_id=doctor_id, day_of_week=day_of_week).first()
        if not availability:
            return jsonify({'error': 'Doctor is not available on this day'}), 400

        # Validate time format
        try:
            appointment_time_obj = datetime.strptime(appointment_time, '%H:%M:%S').time()
        except ValueError:
            return jsonify({'error': 'Invalid time format. Use HH:MM:SS'}), 400

        if not (availability.start_time <= appointment_time_obj <= availability.end_time):
            return jsonify({'error': 'Appointment time is outside doctor availability hours'}), 400

        new_appointment = Appointment(
            patient_id=patient_id,
            doctor_id=doctor_id,
            appointment_date=appointment_date,
            appointment_time=appointment_time_obj,
            status='Scheduled'
        )
        db.session.add(new_appointment)
        db.session.commit()
        return jsonify({'message': 'Appointment scheduled successfully'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
