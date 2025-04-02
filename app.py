from flask import Flask, jsonify
from config import Config
from models import db
from flask_migrate import Migrate
from resources.patient import patient_bp
from resources.auth import auth_bp
from resources.appointment import appointment_bp
from resources.doctor import doctor_bp
from resources.medical_record import medical_record_bp
from swagger import swaggerui_blueprint, create_swagger_json

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(patient_bp, url_prefix='/api/patients')
app.register_blueprint(swaggerui_blueprint, url_prefix='/api/docs')
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(appointment_bp, url_prefix='/api/appointments')
app.register_blueprint(doctor_bp, url_prefix='/api/doctors')
app.register_blueprint(medical_record_bp, url_prefix='/api/medical_records')

@app.route('/static/swagger.json')
def swagger_json():
    return jsonify(create_swagger_json())

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)

