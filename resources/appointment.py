from flask import Blueprint, request, jsonify
from models import db, Appointment, DoctorAvailability, Doctor
from datetime import datetime

appointment_bp = Blueprint('appointment_bp', __name__)

@appointment_bp.route('/', methods=['POST'])
def create_appointment():
    data = request.get_json()
    patient_id = data['patient_id']
    doctor_id = data['doctor_id']
    appointment_date = data['appointment_date']  # Format: YYYY-MM-DD
    appointment_time = data['appointment_time']  # Format: HH:MM:SS

    # Verify doctor exists and has availability on the specified day
    doctor = Doctor.query.get_or_404(doctor_id)
    day_of_week = datetime.strptime(appointment_date, '%Y-%m-%d').strftime('%A')
    availability = DoctorAvailability.query.filter_by(doctor_id=doctor_id, day_of_week=day_of_week).first()
    if not availability:
        return jsonify({'error': 'Doctor is not available on this day'}), 400

    appointment_time_obj = datetime.strptime(appointment_time, '%H:%M:%S').time()
    if not (availability.start_time <= appointment_time_obj <= availability.end_time):
        return jsonify({'error': 'Appointment time is outside doctor availability hours'}), 400

    try:
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

@appointment_bp.route('/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    appointment = Appointment.query.get_or_404(appointment_id)
    return jsonify({
        'id': appointment.id,
        'patient_id': appointment.patient_id,
        'doctor_id': appointment.doctor_id,
        'appointment_date': appointment.appointment_date.isoformat(),
        'appointment_time': appointment.appointment_time.strftime("%H:%M:%S"),
        'status': appointment.status
    })

@appointment_bp.route('/<int:appointment_id>', methods=['PUT'])
def update_appointment(appointment_id):
    appointment = Appointment.query.get_or_404(appointment_id)
    data = request.get_json()
    appointment.status = data.get('status', appointment.status)
    try:
        db.session.commit()
        return jsonify({'message': 'Appointment updated successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@appointment_bp.route('/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    appointment = Appointment.query.get_or_404(appointment_id)
    try:
        db.session.delete(appointment)
        db.session.commit()
        return jsonify({'message': 'Appointment deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
