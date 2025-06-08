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
    "billing": [],
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
        "pat001": [{"treatment": "Surgery", "cost": 4500, "insurance": "10% off"}]
    },
    "reports": [],
    # "efficiency_metrics": [],
    "discharges": [],
}


def register_patient(
    patient_id,
    name,
    age,
    gender,
    medical_history,
    blood_group,
    insurance_name,
    insurance_id,
):
    if patient_id not in hospital_data["patients"]:
        hospital_data["patients"][patient_id] = {
            "patient_id": patient_id,
            "name": name,
            "age": age,
            "gender": gender,
            "medical_history": medical_history,
            "blood_group": blood_group,
            "insurance_info": {"provider": insurance_name, "id": insurance_id},
        }
        return f"""
=== PATIENT DASHBOARD ===
Patient: {name} (ID: {patient_id})
Age: {age} | Gender: {gender} | Blood Type: {blood_group}
Insurance: {insurance_name} (Policy: {insurance_id})
"""
    else:
        return "Patient ID already exists."


# print(register_patient())


def add_medical_staff(
    staff_id, role, name, specialization, start_time, end_time, phone
):
    if staff_id not in hospital_data["staff"]:
        hospital_data["staff"][staff_id] = {
            "id": staff_id,
            "name": name,
            "role": role,
            "specialization": specialization,
            "phone": phone,
            "shift_schedule": {"start_time": start_time, "end_time": end_time},
        }
        return f"\nStaff added successfully with ID: {staff_id}\n"
    return f"\nStaff ID: {staff_id} already exists.\n"


# print(add_medical_staff())


def schedule_appointment(
    patient_id, doctor_id, appointment_date, appointment_time, appointment_type
):
    if patient_id not in hospital_data["patients"]:
        return "\nInvalid patient ID.\n"
    if doctor_id not in hospital_data["staff"]:
        return "\nInvalid doctor ID.\n"

    for a in hospital_data["appointments"]:
        if (
            a["doctor_id"] == doctor_id
            and a["date"] == appointment_date
            and a["time"] == appointment_time
        ):
            return f"\nConflict: Doctor already has an appointment at {appointment_time} on {appointment_date}.\n"

    new_id = str(len(hospital_data["appointments"]) + 1)
    appointment = {
        "id": new_id,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": appointment_date,
        "time": appointment_time,
        "type": appointment_type,
    }
    hospital_data["appointments"].append(appointment)
    return f"\nAppointment scheduled successfully with ID {new_id}.\n"


# print(schedule_appointment())


def create_medical_record(
    patient_id, doctor_id, diagnosis, treatment, prescription, record_date
):
    if patient_id not in hospital_data["patients"]:
        return "Patient ID not found."
    if doctor_id not in hospital_data["staff"]:
        return "Doctor ID not found."

    record_id = str(len(hospital_data["medical_records"]) + 1)
    record = {
        "record_id": record_id,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "diagnosis": diagnosis,
        "treatment": treatment,
        "prescription": prescription,
        "date": record_date,
    }
    hospital_data["medical_records"].append(record)

    print("\n✅ Medical record added successfully!")
    print("------------- Medical Record --------------")
    print(f"Date         : {record['date']}")
    print(f"Patient ID   : {record['patient_id']}")
    print(f"Doctor ID    : {record['doctor_id']}")
    print(f"Diagnosis    : {record['diagnosis']}")
    print(f"Treatment    : {record['treatment']}")
    print(f"Prescription : {record['prescription']}")
    print("-" * 44)
    return f"Medical record created with ID {record_id}."


# print(create_medical_record())


def process_billing(patient_id):
    if patient_id not in hospital_data.get("patients", {}):
        print(f"Patient ID {patient_id} not found in the system.")
        return
    
    if patient_id not in hospital_data.get("treatment_costs", {}):
        print(f"\nNo treatment costs found for Patient ID: {patient_id}")
        print("Please add treatment costs first using the treatment cost")
        return
    patient_info = hospital_data["patients"][patient_id]
    treatments = hospital_data["treatment_costs"][patient_id]

    total_treatment_cost = 0
    for treatment in treatments:
        total_treatment_cost += treatment["cost"]

    additional_charges = {
        "Room Charges": 0,
        "Pharmacy": 0,
        "Lab Fees": 0,
        "Administrative Fee": 50
    }
    print(f"\n=== Processing Bill for Patient: {patient_info['name']} ===")
    print(f"Patient ID: {patient_id}")
    date = input("Enter current date (YYYY-MM-DD): ").strip()
    add_extra = input("\nDo you want to add additional charges? (y/n): ").lower()
    if add_extra == 'y':
        for charge_type in ["Room Charges", "Pharmacy", "Lab Fees"]:
            amount = float(input(f"Enter {charge_type} amount (0 if none): $"))
            additional_charges[charge_type] += amount
    total_additional = sum(additional_charges.values())
    grand_total = total_treatment_cost + total_additional
    
    print("\n" + "="*50)
    print("                    HOSPITAL BILL")
    print("="*50)
    print(f"Patient Name: {patient_info['name']}")
    print(f"Patient ID  : {patient_id}")
    print(f"Phone       : {patient_info.get('age', 'N/A')}")
    print(f"Address     : {patient_info.get('gender', 'N/A')}")
    print("-"*50)
    print("TREATMENT COSTS:")
    print("-"*50)
    i = 1
    for treatment in treatments:
        print(f"{i}. {treatment['treatment']} ${treatment['cost']}")
        print(f"   Insurance: {treatment['insurance']}")
        i += 1
    print(f"Subtotal (Treatments): ${total_treatment_cost}")
    print("-"*50)
    print("ADDITIONAL CHARGES:")
    print("-"*50)
    for charge_type, amount in additional_charges.items():
        if amount > 0:
            print(f"{charge_type} ${amount}")
    print(f"Subtotal (Additional): ${total_additional}")
    print("="*50)
    print(f"GRAND TOTAL: ${grand_total}")
    print("="*50)
    
    if "billing_records" not in hospital_data:
        hospital_data["billing_records"] = {}
    billing_record = {
        "patient_id": patient_id,
        "patient_name": patient_info['name'],
        "treatments": treatments.copy(),
        "additional_charges": additional_charges.copy(),
        "total_treatment_cost": total_treatment_cost,
        "total_additional_cost": total_additional,
        "grand_total": grand_total,
        "billing_date": date
    }
    hospital_data["billing_records"][patient_id] = billing_record
    print(f"\nBilling record saved for Patient ID: {patient_id}")


# print(process_billing())


def manage_emergency_admission(patient_id, emergency_type, severity_level):
    def create_emergency_record():
        if int(severity_level) >= 4:
            emergency = {
                "patient_id": patient_id,
                "type": emergency_type,
                "severity": severity_level,
            }
            return emergency, True
        else:
            return None, False

    if patient_id in hospital_data["patients"]:
        emergency_data, is_emergency = create_emergency_record()
        if is_emergency:
            hospital_data["emergency_cases"].append(emergency_data)
            return f"\nEmergency case recorded. Patient ID: {patient_id}\n"
        else:
            return f"\nPatient ID {patient_id}: Severity level {severity_level} does not qualify for emergency classification.\n"
    else:
        emergency_data, is_emergency = create_emergency_record()
        if is_emergency:
            registration_result = registration()
            new_patient_id = str(len(hospital_data["patients"]))
            emergency_data["patient_id"] = new_patient_id
            hospital_data["emergency_cases"].append(emergency_data)
            return f"Patient registered and emergency case recorded. New Patient ID: {new_patient_id}\n"
        else:
            registration_result = registration()
            return f"\nPatient ID {patient_id}: Severity level {severity_level} does not qualify for emergency classification. Patient registered through standard procedures.\n"


# print(manage_emergency_admission())


def track_medication_inventory(med_id):
    if med_id in hospital_data["inventory"]:
        print(
            f"\nMedication '{med_id}': {hospital_data["inventory"][med_id]["name"]} already exists in the inventory."
        )
        add_qty = int(input("Enter quantity to add: "))
        hospital_data["inventory"][med_id]["quantity"] += add_qty
        print(
            f"Updated quantity for '{med_id}': {hospital_data["inventory"][med_id]["name"]} is now {hospital_data['inventory'][med_id]['quantity']}.\n"
        )
    else:
        name = input("Enter Medication Name: ").title()
        quantity = int(input("Enter Quantity: "))
        expiry = input("Enter Expiry Date (YYYY-MM-DD): ")
        supplier = input("Enter Supplier Name: ")
        hospital_data["inventory"][med_id] = {
            "name": name,
            "quantity": quantity,
            "expiry": expiry,
            "supplier": supplier,
        }
        print(f"\nMedication '{med_id}' added successfully.\n")

    print("Current Medication Inventory:")
    print("-" * 50)
    for med, info in hospital_data["inventory"].items():
        print(f"ID: {med}")
        print(f"  Name     : {info['name']}")
        print(f"  Quantity : {info['quantity']}")
        print(f"  Expiry   : {info['expiry']}")
        print(f"  Supplier : {info['supplier']}")
        print("-" * 50)


# track_medication_inventory()


def assign_room(patient_id):
    if patient_id not in hospital_data["patients"]:
        print(f"\nPatient '{patient_id}' is not registered in the hospital system.\n")
        return
    for room_num, info in hospital_data["room_assignments"].items():
        if info["patient"] == patient_id:
            print(f"\nPatient '{patient_id}' is already assigned to room {room_num}.\n")
            break
    else:
        patient_name = hospital_data["patients"][patient_id]['name']
        print(f"\nAssigning room for patient: {patient_name} (ID: {patient_id})")
        
        room_type = input("Enter Room Type (Private/Shared): ")
        admission_date = input("Enter Admission Date (YYYY-MM-DD): ")
        expected_duration = input("Enter Expected Duration (e.g., 3 days): ")
        room_number = input("Enter Room Number (e.g., 101A): ")

        if room_number in hospital_data["room_assignments"]:
            if hospital_data["room_assignments"][room_number]['room_status'] == 'available':
                hospital_data["room_assignments"][room_number] = {
                    "room_type": room_type,
                    "admission_date": admission_date,
                    "expected_duration": expected_duration,
                    "patient": patient_id,
                    "room_status": "Occupied",
                }
                print(f"\nRoom {room_number} assigned to patient '{patient_name}' (ID: {patient_id}) successfully.\n")
            else:
                print(f'\nRoom no. {room_number} is already occupied!\n')
        else:
            print(f"\nRoom number {room_number} does not exist or is not available.\n")
    
    print("Current Room Assignments:")
    print("-" * 50)
    for room_num, info in hospital_data["room_assignments"].items():
        patient_info = ""
        if info["patient"]:
            patient_name = hospital_data["patients"].get(info["patient"])['name']
            patient_info = f"{info['patient']} ({patient_name})"
        else:
            patient_info = info["patient"]
            
        print(f"Room Number        : {room_num}")
        print(f"  Room Type        : {info['room_type']}")
        print(f"  Admission Date   : {info['admission_date']}")
        print(f"  Expected Duration: {info['expected_duration']}")
        print(f"  Patient          : {patient_info}")
        print(f"  Room Status      : {info['room_status']}")
        print("-" * 50)

# assign_room()


def calculate_treatment_cost(patient_id):
    treatment_catalog = {
        "Basic Checkup": 100,
        "Surgery": 5000,
        "Physiotherapy": 300,
        "Dental Care": 200,
        "X-Ray": 150,
        "Blood Test": 80,
        "Consultation": 120,
        "Vaccination": 75,
        "Prescription": 50,
        "Emergency Care": 500,
    }

    num_treatments = int(input("How many treatments to add? "))
    treatments = []
    total_base_cost = 0

    # Collect all treatments first
    for i in range(num_treatments):
        print(f"\nEntering treatment {i + 1} of {num_treatments}")
        treatment_plan = input(
            f"Enter Treatment Plan ({', '.join(treatment_catalog.keys())}): "
        ).title()

        if treatment_plan not in treatment_catalog:
            print("Invalid treatment plan. Skipping this one.")
            continue

        base_cost = treatment_catalog[treatment_plan]
        treatments.append({"treatment": treatment_plan, "base_cost": base_cost})
        total_base_cost += base_cost

    # Apply single insurance discount to total
    discount_percent = float(
        input(
            f"\nTotal cost before insurance: ${total_base_cost}\n"
            "Enter Insurance Discount (%) [e.g., 10 for 10%]: "
        )
    )

    discount_amount = total_base_cost * (discount_percent / 100)
    total_final_cost = total_base_cost - discount_amount

    # Calculate proportional cost for each treatment
    if patient_id not in hospital_data["treatment_costs"]:
        hospital_data["treatment_costs"][patient_id] = []

    for treatment in treatments:
        # Calculate this treatment's share of the total final cost
        proportion = treatment["base_cost"] / total_base_cost
        treatment_final_cost = total_final_cost * proportion

        treatment_record = {
            "treatment": treatment["treatment"],
            "cost": round(treatment_final_cost, 2),
            "insurance": f"{discount_percent}% off total",
        }
        hospital_data["treatment_costs"][patient_id].append(treatment_record)

    print(f"\nTreatments added successfully!")
    print(f"Total base cost: ${total_base_cost}")
    print(f"Insurance discount: {discount_percent}% (${discount_amount:.2f})")
    print(f"Total final cost: ${total_final_cost:.2f}")

    print("\nPatient Treatment Cost Records:")
    print("-" * 50)
    for pid, treatments in hospital_data["treatment_costs"].items():
        print(f"Patient ID: {pid}")
        patient_total = sum(t["cost"] for t in treatments)
        for i, treatment in enumerate(treatments):
            print(f"  Treatment {i+1}:")
            print(f"    Plan      : {treatment['treatment']}")
            print(f"    Final Cost: ${treatment['cost']}")
            print(f"    Insurance : {treatment['insurance']}")
        print(f"  Total for Patient: ${patient_total:.2f}")
        print("-" * 50)


# calculate_treatment_cost()


def generate_patient_report(patient_id, report_type):
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
        "remarks": remarks,
    }
    hospital_data["reports"].append(report)
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
    return f"Report {report_id} for {patient_name} added successfully.\n"


# print(generate_patient_report())


def analyze_hospital_efficiency():
    metric = {
        "total_patients": len(hospital_data["patients"]),
        "admitted_patients": sum(1 for p in hospital_data["patients"]),
        "emergency_count": len(hospital_data["emergency_cases"]),
    }
    print(f"\n{'-'*35}\n    Hospital Efficiency\n")
    print(f"Total Patients Registered  : {metric['total_patients']}")
    print(f"Currently Admitted Patients: {metric['admitted_patients']}")
    print(f"Emergency Cases            : {metric['emergency_count']}")
    print("-" * 35)


# analyze_hospital_efficiency()


def manage_discharge_process(patient_id, discharge_date, follow_up_instructions):
    if patient_id in hospital_data["patients"]:
        discharge = {
            "patient_id": patient_id,
            "discharge_date": discharge_date,
            "follow_up": follow_up_instructions,
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
        return "Discharge process completed.\n"
    else:
        return "Patient ID not found."


# print(manage_discharge_process())


def registration():
    patient_id = f"{len(hospital_data['patients'])+1}"
    name = input("Enter patient name: ").title()
    age = input("Enter age: ")
    gender = input("Enter gender: ").capitalize()
    medical_history = (
        input("Enter medical history (comma-separated): ").title().split(",")
    )
    blood_group = input("Enter your blood group: ").upper()
    insurance_name = input("Enter insurance provider: ").title()
    insurance_id = input("Enter insurance id: ")
    print(
        register_patient(
            patient_id,
            name,
            age,
            gender,
            medical_history,
            blood_group,
            insurance_name,
            insurance_id,
        )
    )


def main():
    while True:
        print("\n=== Hospital Management System ===")
        print("1. Register Patient")
        print("2. Add Medical Staff")
        print("3. Schedule Appointment")
        print("4. Create Medical Record")
        print("5. Process Billing")
        print("6. Emergency Admission")
        print("7. Track Medication Inventory")
        print("8. Assign Room")
        print("9. Calculate Treatment Cost")
        print("10. Generate Patient Report")
        print("11. Analyze Hospital Efficiency")
        print("12. Manage Discharge Process")
        print("13. Exit\n")
        choice = input("Enter your choice: ")

        if choice == "1":
            registration()

        elif choice == "2":
            staff_id = f"{len(hospital_data['staff'])+1}"
            role = input("Enter role: ").capitalize()
            name = input("Enter name: ").title()
            specialization = input("Enter specialization: ").capitalize()
            start_time = input("Enter shift start time: ")
            end_time = input("Enter shift end time: ")
            phone = input("Enter phone number: ")
            print(
                add_medical_staff(
                    staff_id, role, name, specialization, start_time, end_time, phone
                )
            )

        elif choice == "3":
            patient_id = input("Enter patient ID: ").strip()
            doctor_id = input("Enter doctor ID: ").strip()
            appointment_date = input("Enter appointment date (YYYY-MM-DD): ").strip()
            appointment_time = input(
                "Enter appointment time (HH:MM, 24-hour format): "
            ).strip()
            appointment_type = input("Enter appointment type: ").strip().capitalize()
            print(
                schedule_appointment(
                    patient_id,
                    doctor_id,
                    appointment_date,
                    appointment_time,
                    appointment_type,
                )
            )

        elif choice == "4":
            patient_id = input("Enter patient ID: ").strip()
            doctor_id = input("Enter doctor ID: ").strip()
            diagnosis = input("Enter diagnosis: ").capitalize()
            treatment = input("Enter treatment: ").capitalize()
            prescription = input("Enter prescription: ").capitalize()
            record_date = input("Enter date of record (YYYY-MM-DD): ").strip()
            print(
                create_medical_record(
                    patient_id,
                    doctor_id,
                    diagnosis,
                    treatment,
                    prescription,
                    record_date,
                )
            )

        elif choice == "5":
            print(process_billing())

        elif choice == "6":
            patient_id = input("Enter patient ID: ")
            emergency_type = input("Enter emergency type: ")
            severity_level = input("Enter severity level: ")
            print(
                manage_emergency_admission(patient_id, emergency_type, severity_level)
            )

        elif choice == "7":
            med_id = input("Enter Medication ID: ")
            track_medication_inventory(med_id)

        elif choice == "8":
            patient_id = input("Enter Patient ID: ")
            assign_room(patient_id)

        elif choice == "9":
            patient_id = input("Enter Patient ID: ")
            calculate_treatment_cost(patient_id)

        elif choice == "10":
            patient_id = input("Enter patient ID: ").strip()
            report_type = input("Enter report type (e.g., Blood Test, X-Ray): ").strip()
            print(generate_patient_report(patient_id, report_type))

        elif choice == "11":
            analyze_hospital_efficiency()

        elif choice == "12":
            patient_id = input("Enter patient ID: ").strip()
            discharge_date = input("Enter discharge date (YYYY-MM-DD): ").strip()
            follow_up_instructions = input("Enter follow-up instructions: ").strip()
            print(
                manage_discharge_process(
                    patient_id, discharge_date, follow_up_instructions
                )
            )

        elif choice == "13":
            print("Exiting system.")
            break

        else:
            print("Invalid option. Try again.")


main()
