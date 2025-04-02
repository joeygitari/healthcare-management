# Healthcare Management System

## Overview
The Healthcare Management System is a Flask-based application designed to facilitate medical appointments, patient records, and doctor availability tracking. It provides RESTful APIs for managing patients, doctors, medical records, and appointments.

## Features
- **User Authentication**: Secure login and registration for patients and doctors.
- **Doctor Management**: Store doctor profiles, specializations, and availability.
- **Patient Management**: Register and manage patient details.
- **Appointments**: Schedule, update, and cancel appointments.
- **Medical Records**: Maintain diagnosis, prescriptions, and notes for patients.
- **RESTful API**: Built using Flask with SQLAlchemy for database interactions.

## Tech Stack
- **Backend**: Flask, Flask-RESTful, Flask-SQLAlchemy
- **Database**: PostgreSQL
- **Documentation**: Swagger
- **Authentication**: JWT (JSON Web Token)
- **Testing**: Pytest

## Installation
### Prerequisites
- Python 3.12+
- Virtual environment (optional but recommended)
- PostgreSQL/MySQL database

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/joeygitari/tiberbu.git
   cd tiberbu
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv healthcare-app-env
   source healthcare-app-env/bin/activate  # On Windows use: healthcare-app-env\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables in a `.env` file:
   ```ini
   JWT_SECRET_KEY=your_jwt_secret_key
   SECRET_KEY=your_secret_key
   DATABASE_URL=postgresql://yourusername:yourpassword@localhost:yourport/yourdb
   ```
5. Initialize the database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```
6. Run the application:
   ```bash
   flask run
   ```
   The API will be accessible at `http://127.0.0.1:5000/api/docs`

## API Endpoints
### Authentication
- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login and receive JWT token

### Doctors
- `POST /api/doctors` - Add a new doctor
- `GET /api/doctors` - List all doctors
- `GET /api/doctors/<id>` - Retrieve doctor details
- `PUT /api/doctors/<id>` - Update doctor details
- `DELETE /api/doctors/<id>` - Remove a doctor

### Patients
- `POST /api/patients` - Register a new patient
- `GET /api/patients` - List all patients
- `GET /api/patients/<id>` - Retrieve patient details

### Appointments
- `POST /api/appointments` - Schedule a new appointment
- `GET /api/appointments/<id>` - View appointment details
- `PUT /api/appointments/<id>` - Update appointment status
- `DELETE /api/appointments/<id>` - Cancel an appointment

### Medical Records
- `POST /api/medical_records` - Add medical record
- `GET /api/medical_records/<id>` - View medical record

## Running Tests
To run the test suite, use:
```bash
pytest
```

## Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to your branch (`git push origin feature-branch`)
5. Open a Pull Request
