from flask import Blueprint, request, jsonify
from models import db, Doctor, DoctorAvailability

doctor_bp = Blueprint('doctor_bp', __name__)

@doctor_bp.route('/', methods=['POST'])
def create_doctor():
    data = request.get_json()
    try:
        new_doctor = Doctor(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            phone=data['phone'],
            specialization=data['specialization']
        )
        db.session.add(new_doctor)
        db.session.commit()
        return jsonify({'message': 'Doctor created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@doctor_bp.route('/<int:doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    doctor = Doctor.query.get_or_404(doctor_id)
    availabilities = [{
        'id': avail.id,
        'day_of_week': avail.day_of_week,
        'start_time': avail.start_time.strftime("%H:%M:%S"),
        'end_time': avail.end_time.strftime("%H:%M:%S")
    } for avail in doctor.availabilities]
    
    return jsonify({
        'id': doctor.id,
        'first_name': doctor.first_name,
        'last_name': doctor.last_name,
        'email': doctor.email,
        'phone': doctor.phone,
        'specialization': doctor.specialization,
        'availabilities': availabilities
    })

@doctor_bp.route('/<int:doctor_id>/availability', methods=['POST'])
def add_availability(doctor_id):
    data = request.get_json()
    try:
        new_availability = DoctorAvailability(
            doctor_id=doctor_id,
            day_of_week=data['day_of_week'],
            start_time=data['start_time'],
            end_time=data['end_time']
        )
        db.session.add(new_availability)
        db.session.commit()
        return jsonify({'message': 'Availability added successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
