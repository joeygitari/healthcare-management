from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # URL for exposing Swagger JSON

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Tiberbu Healthcare App API"
    }
)

def create_swagger_json():
    swag = {
        "swagger": "2.0",
        "info": {
            "title": "Tiberbu Healthcare App API",
            "version": "1.0"
        },
        
        "basePath": "/api",
        "paths": {
            "/auth/register": {
                "post": {
                    "summary": "Register a new user",
                    "parameters": [
                        {
                            "in": "body",
                            "name": "body",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "email": {"type": "string"},
                                    "password": {"type": "string"},
                                    "role": {"type": "string"}
                                },
                                "required": ["email", "password"]
                            }
                        }
                    ],
                    "responses": {
                        "201": {"description": "User registered successfully"},
                        "400": {"description": "Error in registration"}
                    }
                }
            },
            "/auth/login": {
                "post": {
                    "summary": "User login",
                    "parameters": [
                        {
                            "in": "body",
                            "name": "body",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "email": {"type": "string"},
                                    "password": {"type": "string"}
                                },
                                "required": ["email", "password"]
                            }
                        }
                    ],
                    "responses": {
                        "200": {"description": "User logged in successfully"},
                        "401": {"description": "Invalid credentials"}
                    }
                }
            },
            "/patients/": {
                "post": {
                    "summary": "Register a new patient",
                    "parameters": [
                        {
                            "in": "body",
                            "name": "body",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "first_name": {"type": "string"},
                                    "last_name": {"type": "string"},
                                    "email": {"type": "string"},
                                    "phone": {"type": "string"},
                                    "gender": {"type": "string"},
                                    "date_of_birth": {"type": "string", "format": "date"},
                                    "insurance_provider": {"type": "string"},
                                    "insurance_number": {"type": "string"}
                                },
                                "required": ["first_name", "last_name", "email", "phone", "insurance_number"]
                            }
                        }
                    ],
                    "responses": {
                        "201": {"description": "Patient registered successfully"},
                        "400": {"description": "Error in registration"}
                    }
                }
            },
            "/doctors/": {
                "post": {
                    "summary": "Create a new doctor profile",
                    "parameters": [
                        {
                            "in": "body",
                            "name": "body",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "first_name": {"type": "string"},
                                    "last_name": {"type": "string"},
                                    "email": {"type": "string"},
                                    "phone": {"type": "string"},
                                    "specialization": {"type": "string"}
                                },
                                "required": ["first_name", "last_name", "email", "phone", "specialization"]
                            }
                        }
                    ],
                    "responses": {
                        "201": {"description": "Doctor created successfully"},
                        "400": {"description": "Error in creation"}
                    }
                }
            },
            "/appointments/": {
                "post": {
                    "summary": "Schedule a new appointment",
                    "parameters": [
                        {
                            "in": "body",
                            "name": "body",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "patient_id": {"type": "integer"},
                                    "doctor_id": {"type": "integer"},
                                    "appointment_date": {"type": "string", "format": "date"},
                                    "appointment_time": {"type": "string", "format": "time"}
                                },
                                "required": ["patient_id", "doctor_id", "appointment_date", "appointment_time"]
                            }
                        }
                    ],
                    "responses": {
                        "201": {"description": "Appointment scheduled successfully"},
                        "400": {"description": "Error in scheduling appointment"}
                    }
                }
            },
            "/medical_records/": {
                "post": {
                    "summary": "Create a new medical record",
                    "parameters": [
                        {
                            "in": "body",
                            "name": "body",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "patient_id": {"type": "integer"},
                                    "appointment_id": {"type": "integer"},
                                    "diagnosis": {"type": "string"},
                                    "prescription": {"type": "string"},
                                    "notes": {"type": "string"}
                                },
                                "required": ["patient_id", "appointment_id"]
                            }
                        }
                    ],
                    "responses": {
                        "201": {"description": "Medical record created successfully"},
                        "400": {"description": "Error in creation"}
                    }
                }
            },
            
        }
    }
    return swag
