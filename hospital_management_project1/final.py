hospital_data = {
    "patients": {'1': {
    "patient_id": "1",
    "name": "Ravi Kumar",
    "age": "45",
    "gender": "Male",
    "medical_history": ["Diabetes", "Hypertension"],
    "blood_group": "B+",
    "insurance_name": "HealthSecure Pvt Ltd",
    "insurance_id": "HSPL123456"
}},
    "staff": {
    "1": {
      "id": '1',
      "name": "Dr. Alice Sharma",
      "role": "Doctor",
      "specialization": "General Medicine",
      "phone": "9876543210",
      "shift": {
        "start": "09:00",
        "end": "17:00"
      }
    },
    "2": {
      "id": '2',
      "name": "navya",
      "role": "Nurse",
      "specialization": "Emergency",
      "phone": "9876543211",
      "shift": {
        "start": "07:00",
        "end": "15:00"
      }
    },
    "3": {
      "id": '3',
      "name": "Meena Kapoor",
      "role": "Receptionist",
      "specialization": "Front Desk",
      "phone": "9876543212",
      "shift": {
        "start": "08:00",
        "end": "16:00"
      }
    },
    "4": {
      "id": '4',
      "name": "Dr. Vikram Rao",
      "role": "Surgeon",
      "specialization": "Surgery",
      "phone": "9876543213",
      "shift": {
        "start": "14:00",
        "end": "22:00"
      }
    }
  },
    "appointments": [
    {
      "patient_id": "1",
      "doctor_id": "1",
      "date": "2025-06-01",
      "time": "10:00",
      "type": "General Checkup"
    },
    {
      "patient_id": "1",
      "doctor_id": "4",
      "date": "2025-06-03",
      "time": "19:00",
      "type": "Surgery Consultation"
    }
  ]
}


def register_patient():
    patient_id = input("Enter patient ID: ")
    name = input("Enter patient name: ").title()
    age = input("Enter age: ")
    gender = input("Enter gender: ").capitalize()
    medical_history = input("Enter medical history (comma-separated): ").title().split(",")
    blood_group = input('Enter your blood group: ').upper()
    insurance_name = input("Enter insurance provider: ").title()
    insurance_id = input("Enter insurance id: ")

    if patient_id not in hospital_data["patients"]:
        hospital_data["patients"][patient_id] = {
            "personal_info": {"name": name, "age": age, 'gender': gender},
            "medical_history": medical_history,
            "blood_group": blood_group,
            "insurance_info": {"provider": insurance_name, "id": insurance_id}
        }
        # return "Patient registered successfully."
        return f'''
    === PATIENT DASHBOARD ===
    Patient: {name} (ID: {patient_id})
    Age: {age} | Gender: {gender} | Blood Type: {blood_group}
    Insurance: {insurance_name} (Policy: {insurance_id})
    '''
    else:
        return "Patient ID already exists."
# print(register_patient())


def add_medical_staff():
    staff_id = input("Enter staff ID: ")
    name = input("Enter name: ").title()
    role = input("Enter role: ").capitalize()
    specialization = input("Enter specialization: ").capitalize()
    start_time = input("Enter shift start time: ")
    end_time = input("Enter shift end time: ")
    phone = input("Enter phone number: ")

    if staff_id not in hospital_data["staff"]:
        hospital_data["staff"][staff_id] = {
            'id': staff_id,
            "name": name,
            'role': role,
            "specialization": specialization,
            "phone": phone,
            "shift_schedule": {
                'start_time': start_time,
                'end_time': end_time
            }
        }
        return "Staff added successfully."
    return "Staff ID already exists."
# print(add_medical_staff())


def schedule_appointment():
    patient_id = input("Enter patient ID: ").strip()
    doctor_id = input("Enter doctor ID: ").strip()
    appointment_date = input("Enter appointment date (YYYY-MM-DD): ").strip()
    appointment_time = input("Enter appointment time (HH:MM, 24-hour format): ").strip()
    appointment_type = input("Enter appointment type: ").strip().capitalize()

    if patient_id not in hospital_data["patients"]:
        return "Invalid patient ID."

    if doctor_id not in hospital_data["staff"]:
        return "Invalid doctor ID."

    for a in hospital_data["appointments"]:
        if (
            a["doctor_id"] == doctor_id and
            a["date"] == appointment_date and
            a["time"] == appointment_time
        ):
            return f"Conflict: Doctor already has an appointment at {appointment_time} on {appointment_date}."

    new_id = str(len(hospital_data["appointments"]) + 1)
    appointment = {
        "id": new_id,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": appointment_date,
        "time": appointment_time,
        "type": appointment_type
    }
    hospital_data["appointments"].append(appointment)
    return f"Appointment scheduled successfully with ID {new_id}."
# print(schedule_appointment())


