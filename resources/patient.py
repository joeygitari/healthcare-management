from flask import Blueprint, request, jsonify
from models import db, Patient

patient_bp = Blueprint('patient_bp', __name__)

@patient_bp.route('/', methods=['POST'])
def register_patient():
    data = request.get_json()
    try:
        new_patient = Patient(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            phone=data['phone'],
            gender=data.get('gender'),
            date_of_birth=data.get('date_of_birth'),
            insurance_provider=data.get('insurance_provider'),
            insurance_number=data['insurance_number']
        )
        db.session.add(new_patient)
        db.session.commit()
        return jsonify({'message': 'Patient registered successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@patient_bp.route('/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    return jsonify({
        'id': patient.id,
        'first_name': patient.first_name,
        'last_name': patient.last_name,
        'email': patient.email,
        'phone': patient.phone,
        'gender': patient.gender,
        'date_of_birth': patient.date_of_birth.isoformat() if patient.date_of_birth else None,
        'insurance_provider': patient.insurance_provider,
        'insurance_number': patient.insurance_number
    })
