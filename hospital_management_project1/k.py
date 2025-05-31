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
  ],
    "medical_records": [{
        "record_id": "1",
        "patient_id": "1",
        "doctor_id": "1",
        "diagnosis": "High Blood Pressure",
        "treatment": "Low-sodium diet, daily walking",
        "prescription": "Amlodipine 5mg once daily",
        "date": "2025-05-28"
    }],
    "billing": [],
    "emergency_cases": [],
    "medication_inventory": {"MED001": {
        "quantity": 200,
        "expiry_date": "2025-12-31",
        "supplier": "HealthMed Pvt Ltd"
    },
    "MED002": {
        "quantity": 100,
        "expiry_date": "2026-03-15",
        "supplier": "PharmaCare Distributors"
    }},
    "room_assignments": {"101": {
        "patient_id": "1",
        "patient_name": "Ravi Kumar",
        "room_type": "General",
        "admission_date": "2025-05-25",
        "discharge_date": "",
        "status": "Occupied"
    },
    "102": {
        "patient_id": "",
        "patient_name": "",
        "room_type": "Private",
        "admission_date": "",
        "discharge_date": "",
        "status": "Available"
    },
    "103": {
        "patient_id": "",
        "patient_name": "",
        "room_type": "General",
        "admission_date": "",
        "discharge_date": "",
        "status": "Available"
    }},
    "treatment_costs": {},
    "reports": [],
    "discharges": [],
    "efficiency_metrics": []
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


def create_medical_record():
    patient_id = input("Enter patient ID: ").strip()
    doctor_id = input("Enter doctor ID: ").strip()
    diagnosis = input("Enter diagnosis: ").capitalize()
    treatment = input("Enter treatment: ").capitalize()
    prescription = input("Enter prescription: ").capitalize()
    record_date = input("Enter date of record (YYYY-MM-DD): ").strip()

    if patient_id not in hospital_data["patients"]:
        return "Error: Patient ID not found."

    if doctor_id not in hospital_data["staff"]:
        return "Error: Doctor ID not found."

    record_id = str(len(hospital_data["medical_records"]) + 1)
    record = {
        "record_id": record_id,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "diagnosis": diagnosis,
        "treatment": treatment,
        "prescription": prescription,
        "date": record_date
    }
    hospital_data["medical_records"].append(record)
    return f"Medical record created successfully with ID {record_id}."
# print(create_medical_record())


def process_billing():
    patient_id = input("Enter patient ID: ").strip()
    if patient_id not in hospital_data["patients"]:
        return "Patient ID not found."

    patient = hospital_data["patients"][patient_id]
    patient_name = patient["name"]
    admission_date = input("Enter admission date (e.g., March 15, 2025): ").strip()
    discharge_date = input("Enter discharge date (e.g., March 18, 2025): ").strip()
    num_services = int(input("How many services do you want to enter? "))
    services = []
    total_cost = 0

    for i in range(num_services):
        desc = input(f"Enter description for service {i+1}: ").strip().capitalize()
        cost_str = input(f"Enter cost for '{desc}': ").strip()
        cost = float(cost_str)
        services.append({"description": desc, "cost": cost})
        total_cost += cost

    insurance_str = input("Enter insurance coverage percentage (e.g., 10): ").strip()
    insurance_coverage = float(insurance_str)
    discount = (insurance_coverage / 100) * total_cost
    final_cost = total_cost - discount

    billing_info = {
        "patient_id": patient_id,
        "patient_name": patient_name,
        "admission_date": admission_date,
        "discharge_date": discharge_date,
        "services": services,
        "total_cost": total_cost,
        "insurance_coverage": insurance_coverage,
        "final_cost": final_cost
    }
    hospital_data["billing"].append(billing_info)

    print("\n=== BILLING SUMMARY ===")
    print("Patient:", patient_name)
    print("Admission Date:", admission_date)
    print("Discharge Date:", discharge_date)
    print("Service Charges:")
    for service in services:
        print(f"{service['description']}: ₹{service['cost']}")
    print(f"Total Cost: ₹{total_cost}")
    print(f"Insurance Coverage: {insurance_coverage}%")
    print(f"Final Amount Payable: ₹{final_cost}")
    return "Billing processed successfully."
# print(process_billing())


def manage_emergency_admission():
    patient_id = input("Enter patient ID: ")
    emergency_type = input("Enter emergency type: ")
    severity_level = input("Enter severity level: ")

    if patient_id in hospital_data["patients"]:
        emergency = {
            "patient_id": patient_id,
            "type": emergency_type,
            "severity": severity_level
        }
        hospital_data["emergency_cases"].append(emergency)
        return "Emergency case recorded."
    else:
        return "Patient ID not found."
# print(manage_emergency_admission())


def track_medication_inventory():
    medication_id = input("Enter medication ID: ").upper()
    quantity = int(input("Enter quantity: "))
    expiry_date = input("Enter expiry date (YYYY-MM-DD): ")
    supplier = input("Enter supplier name: ").capitalize()

    if medication_id in hospital_data["medication_inventory"]:
        hospital_data["medication_inventory"][medication_id]["quantity"] += quantity
    else:
        hospital_data["medication_inventory"][medication_id] = {
            "quantity": quantity,
            "expiry_date": expiry_date,
            "supplier": supplier
        }
    return "Inventory updated."
# print(track_medication_inventory())


def assign_room():
    patient_id = input("Enter patient ID: ").strip()
    room_type = input("Enter room type (e.g., General, Private): ").strip().capitalize()
    admission_date = input("Enter admission date (YYYY-MM-DD): ").strip()

    if patient_id not in hospital_data["patients"]:
        return "Patient ID not found."

    for room_number, room_info in hospital_data["room_assignments"].items():
        if room_info["status"] == "Available" and room_info["room_type"].lower() == room_type.lower():
            hospital_data["room_assignments"][room_number] = {
                "patient_id": patient_id,
                "patient_name": hospital_data["patients"][patient_id]["name"],
                "room_type": room_type,
                "admission_date": admission_date,
                "discharge_date": "",
                "status": "Occupied"
            }
            return f"Room {room_number} assigned to patient {hospital_data['patients'][patient_id]['name']}."
    return f"No {room_type} rooms available right now."
# print(assign_room())


def calculate_treatment_cost():
    patient_id = input("Enter patient ID: ").strip()
    if patient_id not in hospital_data["patients"]:
        return "Patient ID not found."

    patient_name = hospital_data["patients"][patient_id]["name"]
    num_items = int(input("Enter number of treatments in the plan: "))
    treatment_plan = []
    base_cost = 0

    for i in range(num_items):
        treatment_name = input(f"Enter name of treatment {i+1}: ").strip()
        cost = float(input(f"Enter cost for {treatment_name}: "))
        treatment_plan.append({"treatment": treatment_name, "cost": cost})
        base_cost += cost

    insurance_coverage = float(input("Enter insurance coverage percentage: ").strip())
    discount = (insurance_coverage / 100) * base_cost
    final_cost = base_cost - discount

    hospital_data["treatment_costs"][patient_id] = {
        "patient_name": patient_name,
        "treatments": treatment_plan,
        "base_cost": base_cost,
        "insurance_coverage": insurance_coverage,
        "final_cost": final_cost
    }
    # Print cost breakdown
    print("\n=== TREATMENT COST SUMMARY ===")
    print("Patient:", patient_name)
    print("Treatments:")
    for item in treatment_plan:
        print(f"- {item['treatment']}: ₹{item['cost']}")
    print(f"Base Cost: ₹{base_cost}")
    print(f"Insurance Coverage: {insurance_coverage}%")
    print(f"Final Amount Payable: ₹{final_cost}")
    return "Treatment cost calculated successfully."
# print(calculate_treatment_cost())


def generate_patient_report():
    patient_id = input("Enter patient ID: ").strip()
    report_type = input("Enter report type (e.g., Blood Test, X-Ray): ").strip()
    if patient_id not in hospital_data["patients"]:
        return "Patient ID not found."

    report_id = "REP" + str(len(hospital_data["reports"]) + 1).zfill(3)
    patient_name = hospital_data["patients"][patient_id]["name"]
    report_date = input("Enter report date (YYYY-MM-DD): ").strip()
    doctor_id = input("Enter doctor ID: ").strip()
    if doctor_id not in hospital_data["staff"]:
        return "Doctor ID not found."
    doctor_name = hospital_data["staff"][doctor_id]["name"]

    num_entries = int(input("Enter number of detail entries in report: "))
    details = {}
    for _ in range(num_entries):
        key = input("Enter detail name (e.g., Hemoglobin, Findings): ").strip()
        value = input(f"Enter value for {key}: ").strip()
        details[key] = value
    remarks = input("Enter doctor's remarks: ").strip()

    report = {
        "report_id": report_id,
        "patient_id": patient_id,
        "patient_name": patient_name,
        "report_type": report_type,
        "report_date": report_date,
        "details": details,
        "doctor_id": doctor_id,
        "doctor_name": doctor_name,
        "remarks": remarks
    }
    hospital_data["reports"].append(report)# === Formatted Report Output ===
    print("\n====== MEDICAL REPORT ======")
    print(f"Report ID     : {report_id}")
    print(f"Report Type   : {report_type}")
    print(f"Report Date   : {report_date}")
    print(f"Patient ID    : {patient_id}")
    print(f"Patient Name  : {patient_name}")
    print(f"Doctor ID     : {doctor_id}")
    print(f"Doctor Name   : {doctor_name}")
    print("\n-- Report Details --")
    for key in details:
        print(f"{key}: {details[key]}")
    print("\nRemarks:", remarks)
    print("============================\n")
    return f"Report {report_id} for {patient_name} added successfully."
# print(generate_patient_report())


def analyze_hospital_efficiency():
    metrics_type = input("Enter metrics type (e.g., Patient Turnover): ")
    time_period = input("Enter time period (e.g., Monthly): ")

    result = f"Analyzing {metrics_type} over {time_period}..."
    hospital_data["efficiency_metrics"].append({
        "type": metrics_type,
        "period": time_period,
        "result": result
    })
    return result
# print(analyze_hospital_efficiency())


def manage_discharge_process():
    patient_id = input("Enter patient ID: ").strip()
    discharge_date = input("Enter discharge date (YYYY-MM-DD): ").strip()
    follow_up_instructions = input("Enter follow-up instructions: ").strip()
    
    if patient_id in hospital_data["patients"]:
        discharge = {
            "patient_id": patient_id,
            "discharge_date": discharge_date,
            "follow_up": follow_up_instructions
        }
        hospital_data["discharges"].append(discharge)

        for room in hospital_data["room_assignments"]:
            room_info = hospital_data["room_assignments"][room]
            if room_info.get("patient_id") == patient_id:
                room_info["patient_id"] = ""
                room_info["patient_name"] = ""
                room_info["discharge_date"] = ""
                room_info["status"] = "Available"
                break

        print("\n=== DISCHARGE SUMMARY ===")
        print(f"Patient ID       : {patient_id}")
        print(f"Patient name     : {hospital_data['patients'][patient_id]['name']}")
        print(f"Discharge Date   : {discharge_date}")
        print(f"Follow-up        : {follow_up_instructions}")
        print("Room status      : Updated to 'Available'")
        print("==========================\n")
        return "Discharge process completed."
    else:
        return "Patient ID not found."
print(manage_discharge_process())
