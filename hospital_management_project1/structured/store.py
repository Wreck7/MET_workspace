hospital_data = {
    "patients": {
        "1": {
            "patient_id": "1",
            "name": "Harry Potter",
            "age": "23",
            "gender": "Male",
            "medical_history": ["Diabetes", "Hypertension"],
            "blood_group": "O+",
            "insurance_name": "Expert Pvt Ltd",
            "insurance_id": "HPL7707",
        },
    },
    "staff": {
        "1": {
            "id": "1",
            "name": "Dr. Hermoine granger",
            "role": "Doctor",
            "specialization": "General Medicine",
            "phone": "9876543210",
            "shift": {"start": "09:00", "end": "17:00"},
        },
        "2": {
            "id": "2",
            "name": "navya",
            "role": "Nurse",
            "specialization": "Emergency",
            "phone": "9876543211",
            "shift": {"start": "07:00", "end": "15:00"},
        },
        "3": {
            "id": "3",
            "name": "Meena Kapoor",
            "role": "Receptionist",
            "specialization": "Front Desk",
            "phone": "9876543212",
            "shift": {"start": "08:00", "end": "16:00"},
        },
        "4": {
            "id": "4",
            "name": "Dr. Ron Weasley",
            "role": "Surgeon",
            "specialization": "Surgery",
            "phone": "9876543213",
            "shift": {"start": "14:00", "end": "22:00"},
        },
    },
    "appointments": [
        {
            "patient_id": "1",
            "doctor_id": "1",
            "date": "2025-06-01",
            "time": "10:00",
            "type": "General Checkup",
        },
        {
            "patient_id": "1",
            "doctor_id": "4",
            "date": "2025-06-03",
            "time": "19:00",
            "type": "Surgery Consultation",
        },
    ],
    "medical_records": [
        {
            "record_id": "1",
            "patient_id": "1",
            "doctor_id": "1",
            "diagnosis": "High Blood Pressure",
            "treatment": "Low-sodium diet, daily walking",
            "prescription": "Amlodipine 5mg once daily",
            "date": "2025-05-28",
        }
    ],
    "billing": {},
    "emergency_cases": [],
    "inventory": {
        "m1": {
            "name": "Paracetamol",
            "quantity": 100,
            "expiry": "2025-12-31",
            "supplier": "MediCorp",
        },
        "m2": {
            "name": "Amoxicillin",
            "quantity": 50,
            "expiry": "2024-11-15",
            "supplier": "HealthPharma",
        },
    },
    "room_assignments": {
        "101A": {
            "room_type": "Private",
            "admission_date": "2025-05-01",
            "expected_duration": "5 days",
            "patient": "1",
            "room_status": "Occupied",
        },
        "202B": {
            "room_type": "Shared",
            "admission_date": "",
            "expected_duration": "",
            "patient": "",
            "room_status": "available",
        },
    },
    "treatment_costs": {
        "1": [{"treatment": "Surgery", "cost": 4500, "insurance": "10% off"}]
    },
    "reports": [],
    # "efficiency_metrics": [],
    "discharges": [],
}
