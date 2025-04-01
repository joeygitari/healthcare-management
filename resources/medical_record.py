from flask import Blueprint, request, jsonify
from models import db, MedicalRecord

medical_record_bp = Blueprint('medical_record_bp', __name__)

@medical_record_bp.route('/', methods=['POST'])
def create_medical_record():
    data = request.get_json()
    try:
        new_record = MedicalRecord(
            patient_id=data['patient_id'],
            appointment_id=data['appointment_id'],
            diagnosis=data.get('diagnosis', ''),
            prescription=data.get('prescription', ''),
            notes=data.get('notes', '')
        )
        db.session.add(new_record)
        db.session.commit()
        return jsonify({'message': 'Medical record created successfully', 'record': new_record.serialize()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@medical_record_bp.route('/<int:record_id>', methods=['GET'])
def get_medical_record(record_id):
    record = MedicalRecord.query.get_or_404(record_id)
    return jsonify(record.serialize())

@medical_record_bp.route('/<int:record_id>', methods=['PUT'])
def update_medical_record(record_id):
    record = MedicalRecord.query.get_or_404(record_id)
    data = request.get_json()
    record.diagnosis = data.get('diagnosis', record.diagnosis)
    record.prescription = data.get('prescription', record.prescription)
    record.notes = data.get('notes', record.notes)
    try:
        db.session.commit()
        return jsonify({'message': 'Medical record updated successfully', 'record': record.serialize()})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@medical_record_bp.route('/<int:record_id>', methods=['DELETE'])
def delete_medical_record(record_id):
    record = MedicalRecord.query.get_or_404(record_id)
    try:
        db.session.delete(record)
        db.session.commit()
        return jsonify({'message': 'Medical record deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
