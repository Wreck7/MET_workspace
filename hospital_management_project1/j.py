hospital_data = {
    "patients": {
        "1": {
            "name": "Ravi Kumar",
            "age": "45",
            "gender": "Male",
            "medical_history": ["Diabetes", "Hypertension"],
            "blood_group": "B+",
            "insurance_name": "HealthSecure Pvt Ltd",
            "insurance_id": "HSPL123456",
        },
    },
    "staff": {
        "1": {
            "name": "Dr. Alice Sharma",
            "role": "Doctor",
            "specialization": "General Medicine",
            "phone": "9876543210",
            "shift": {"start": "09:00", "end": "17:00"},
        },
        "2": {
            "name": "navya",
            "role": "Nurse",
            "specialization": "Emergency",
            "phone": "9876543211",
            "shift": {"start": "07:00", "end": "15:00"},
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
        "m01": {
            "name": "Paracetamol",
            "quantity": 100,
            "expiry": "2025-12-31",
            "supplier": "MediCorp",
        },
    },
    "room_assignments": {
        "1": {
            "room_type": "Private",
            "admission_date": "2025-05-01",
            "expected_duration": "5 days",
            "room_number": "101A",
            "room_status": "Occupied",
        },
    },
    "treatment_costs": {
        "pat001": [{"treatment": "Surgery", "cost": 4500, "insurance": "10% off"}]
    },
    "reports": [],
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
    if patient_id in hospital_data["patients"]:
        return "Patient ID already exists."
    hospital_data["patients"][patient_id] = {
        "name": name,
        "age": age,
        "gender": gender,
        "medical_history": medical_history,
        "blood_group": blood_group,
        "insurance_name": insurance_name,
        "insurance_id": insurance_id,
    }
    return f"""
=== PATIENT DASHBOARD ===
Patient: {name} (ID: {patient_id})
Age: {age} | Gender: {gender} | Blood Type: {blood_group}
Insurance: {insurance_name} (Policy: {insurance_id})
"""


def add_medical_staff(
    staff_id, role, name, specialization, start_time, end_time, phone
):
    if staff_id in hospital_data["staff"]:
        return "Staff ID already exists."
    hospital_data["staff"][staff_id] = {
        "id": staff_id,
        "name": name,
        "role": role,
        "specialization": specialization,
        "phone": phone,
        "shift": {"start": start_time, "end": end_time},
    }
    return "Staff added successfully."


def schedule_appointment(
    patient_id, doctor_id, appointment_date, appointment_time, appointment_type
):
    if patient_id not in hospital_data["patients"]:
        return "Invalid patient ID."
    if doctor_id not in hospital_data["staff"]:
        return "Invalid doctor ID."
    for appt in hospital_data["appointments"]:
        if (
            appt["doctor_id"] == doctor_id
            and appt["date"] == appointment_date
            and appt["time"] == appointment_time
        ):
            return f"Conflict: Doctor already has an appointment at {appointment_time} on {appointment_date}."
    new_id = str(len(hospital_data["appointments"]) + 1)
    hospital_data["appointments"].append(
        {
            "id": new_id,
            "patient_id": patient_id,
            "doctor_id": doctor_id,
            "date": appointment_date,
            "time": appointment_time,
            "type": appointment_type,
        }
    )
    return f"Appointment scheduled successfully with ID {new_id}."


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
    return f"""
✅ Medical record added successfully!
------------- Medical Record --------------
Patient ID   : {record['patient_id']}
Doctor ID    : {record['doctor_id']}
Diagnosis    : {record['diagnosis']}
Treatment    : {record['treatment']}
Prescription : {record['prescription']}
-------------------------------------------
Medical record created with ID {record_id}.
"""


def process_billing():
    patient_id = input("Enter patient ID: ").strip()
    if patient_id not in hospital_data["patients"]:
        return "Patient ID not found."

    patient_name = hospital_data["patients"][patient_id]["name"]
    admission_date = input("Enter admission date (e.g., March 15, 2025): ").strip()
    discharge_date = input("Enter discharge date (e.g., March 18, 2025): ").strip()

    num_services = int(input("How many services do you want to enter? "))
    services = []
    total_cost = 0
    for i in range(num_services):
        desc = input(f"Enter description for service {i+1}: ").strip().capitalize()
        cost = float(input(f"Enter cost for '{desc}': ").strip())
        services.append({"description": desc, "cost": cost})
        total_cost += cost

    insurance_coverage = float(
        input("Enter insurance coverage percentage (e.g., 10): ").strip()
    )
    final_cost = total_cost * (1 - insurance_coverage / 100)

    billing_info = {
        "patient_id": patient_id,
        "patient_name": patient_name,
        "admission_date": admission_date,
        "discharge_date": discharge_date,
        "services": services,
        "total_cost": total_cost,
        "insurance_coverage": insurance_coverage,
        "final_cost": final_cost,
    }
    hospital_data["billing"].append(billing_info)

    return f"""
=== BILLING SUMMARY ===
Patient: {patient_name}
Admission Date: {admission_date}
Discharge Date: {discharge_date}
Service Charges:
{chr(10).join([f"{s['description']}: ₹{s['cost']}" for s in services])}
Total Cost: ₹{total_cost}
Insurance Coverage: {insurance_coverage}%
Final Amount Payable: ₹{final_cost}
--------------------------------------------------
Billing processed successfully.
"""


def manage_emergency_admission(patient_id, emergency_type, severity_level):
    if patient_id not in hospital_data["patients"]:
        return "Patient ID not found."
    hospital_data["emergency_cases"].append(
        {
            "patient_id": patient_id,
            "type": emergency_type,
            "severity": severity_level,
        }
    )
    return f"Emergency case recorded. Patient ID: {patient_id}\n"


def track_medication_inventory(med_id):
    if med_id in hospital_data["inventory"]:
        add_qty = int(
            input(f"Medication '{med_id}' already exists. Enter quantity to add: ")
        )
        hospital_data["inventory"][med_id]["quantity"] += add_qty
        print(
            f"Updated quantity for '{med_id}' is now {hospital_data['inventory'][med_id]['quantity']}.\n"
        )
    else:
        name = input("Enter Medication Name: ")
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

    print("--- Current Medication Inventory ---")
    for med, info in hospital_data["inventory"].items():
        print(
            f"ID: {med}\n  Name: {info['name']}\n  Quantity: {info['quantity']}\n  Expiry: {info['expiry']}\n  Supplier: {info['supplier']}\n"
            + "-" * 36
        )


def assign_room(patient_id):
    if (
        patient_id in hospital_data["room_assignments"]
        and hospital_data["room_assignments"][patient_id]["room_status"] == "Occupied"
    ):
        return f"\nPatient '{patient_id}' is already assigned and occupying a room.\n"

    room_type = input("Enter Room Type (Private/Shared): ")
    admission_date = input("Enter Admission Date (YYYY-MM-DD): ")
    expected_duration = input("Enter Expected Duration (e.g., 3 days): ")
    room_number = input("Enter Room Number (e.g., 101A): ")

    hospital_data["room_assignments"][patient_id] = {
        "room_type": room_type,
        "admission_date": admission_date,
        "expected_duration": expected_duration,
        "room_number": room_number,
        "room_status": "Occupied",
    }
    print(f"\nRoom assigned to patient '{patient_id}' successfully.\n")

    print("--- Current Room Assignments ---")
    for pid, info in hospital_data["room_assignments"].items():
        print(
            f"Patient ID: {pid}\n  Room Type: {info['room_type']}\n  Admission Date: {info['admission_date']}\n  Expected Duration: {info['expected_duration']}\n  Room Number: {info['room_number']}\n  Room Status: {info['room_status']}\n"
            + "-" * 34
        )


def calculate_treatment_cost(patient_id):
    treatment_catalog = {
        "Basic Checkup": 100,
        "Surgery": 5000,
        "Physiotherapy": 300,
        "Dental Care": 200,
    }
    num_treatments = int(input("How many treatments to add? "))

    if patient_id not in hospital_data["treatment_costs"]:
        hospital_data["treatment_costs"][patient_id] = []

    for i in range(num_treatments):
        treatment_plan = input(
            f"Enter Treatment Plan ({', '.join(treatment_catalog.keys())}) for treatment {i+1}: "
        ).title()
        if treatment_plan not in treatment_catalog:
            print("Invalid treatment plan. Skipping this one.")
            continue

        base_cost = treatment_catalog[treatment_plan]
        discount_percent = float(
            input("Enter Insurance Discount (%) [e.g., 10 for 10%]: ")
        )
        final_cost = base_cost * (1 - discount_percent / 100)

        hospital_data["treatment_costs"][patient_id].append(
            {
                "treatment": treatment_plan,
                "cost": round(final_cost, 2),
                "insurance": f"{discount_percent}% off",
            }
        )
        print("Treatment added.")

    print("\n--- Patient Treatment Cost Records ---")
    for pid, treatments in hospital_data["treatment_costs"].items():
        print(f"Patient ID: {pid}")
        for i, info in enumerate(treatments, 1):
            print(
                f"  Treatment {i}:\n    Plan: {info['treatment']}\n    Final Cost: ${info['cost']}\n    Insurance: {info['insurance']}"
            )
        print("-" * 36)


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
    details = {
        input("Enter detail name: ").strip(): input("Enter value: ").strip()
        for _ in range(num_entries)
    }
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

    return f"""
====== MEDICAL REPORT ======
Report ID: {report_id}
Report Type: {report_type}
Report Date: {report_date}
Patient ID: {patient_id}
Patient Name: {patient_name}
Doctor ID: {doctor_id}
Doctor Name: {doctor_name}

-- Report Details --
{chr(10).join([f"{k}: {v}" for k, v in details.items()])}

Remarks: {remarks}
============================
Report {report_id} for {patient_name} added successfully.
"""


def analyze_hospital_efficiency():
    metrics = {
        "total_patients": len(hospital_data["patients"]),
        "admitted_patients": sum(
            1
            for p_id, r_info in hospital_data["room_assignments"].items()
            if r_info["room_status"] == "Occupied"
        ),
        "emergency_count": len(hospital_data["emergency_cases"]),
    }
    return f"""
-----------------------------------
        Hospital Efficiency
-----------------------------------
Total Patients Registered  : {metrics['total_patients']}
Currently Admitted Patients: {metrics['admitted_patients']}
Emergency Cases            : {metrics['emergency_count']}
-----------------------------------
"""


def manage_discharge_process(patient_id, discharge_date, follow_up_instructions):
    if patient_id not in hospital_data["patients"]:
        return "Patient ID not found."

    hospital_data["discharges"].append(
        {
            "patient_id": patient_id,
            "discharge_date": discharge_date,
            "follow_up": follow_up_instructions,
        }
    )

    # Update room status
    for room_id, room_info in hospital_data["room_assignments"].items():
        # Check if the room is occupied by the patient being discharged
        if room_id == patient_id and room_info["room_status"] == "Occupied":
            room_info["room_status"] = "Available"
            # Clear patient-specific information for the now-available room
            room_info["admission_date"] = ""
            room_info["expected_duration"] = ""
            # Note: We are not removing the room from room_assignments, just updating its status and details.
            break

    return f"""
=== DISCHARGE SUMMARY ===
Patient ID: {patient_id}
Patient Name: {hospital_data['patients'][patient_id]['name']}
Discharge Date: {discharge_date}
Follow-up: {follow_up_instructions}
Room status: Updated to 'Available' (if applicable)
==========================
Discharge process completed.
"""


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
            pid = input("Enter patient ID: ")
            name = input("Enter patient name: ").title()
            age = input("Enter age: ")
            gender = input("Enter gender: ").capitalize()
            medical_history = [
                h.strip()
                for h in input("Enter medical history (comma-separated): ")
                .title()
                .split(",")
            ]
            blood_group = input("Enter blood group: ").upper()
            insurance_name = input("Enter insurance provider: ").title()
            insurance_id = input("Enter insurance ID: ")
            print(
                register_patient(
                    pid,
                    name,
                    age,
                    gender,
                    medical_history,
                    blood_group,
                    insurance_name,
                    insurance_id,
                )
            )

        elif choice == "2":
            sid = input("Enter staff ID: ")
            role = input("Enter role: ").capitalize()
            name = input("Enter name: ").title()
            specialization = input("Enter specialization: ").capitalize()
            start_time = input("Enter shift start time (HH:MM): ")
            end_time = input("Enter shift end time (HH:MM): ")
            phone = input("Enter phone number: ")
            print(
                add_medical_staff(
                    sid, role, name, specialization, start_time, end_time, phone
                )
            )

        elif choice == "3":
            pid = input("Enter patient ID: ").strip()
            did = input("Enter doctor ID: ").strip()
            date = input("Enter appointment date (YYYY-MM-DD): ").strip()
            time = input("Enter appointment time (HH:MM, 24-hour format): ").strip()
            app_type = input("Enter appointment type: ").strip().capitalize()
            print(schedule_appointment(pid, did, date, time, app_type))

        elif choice == "4":
            pid = input("Enter patient ID: ").strip()
            did = input("Enter doctor ID: ").strip()
            diagnosis = input("Enter diagnosis: ").capitalize()
            treatment = input("Enter treatment: ").capitalize()
            prescription = input("Enter prescription: ").capitalize()
            rec_date = input("Enter date of record (YYYY-MM-DD): ").strip()
            print(
                create_medical_record(
                    pid, did, diagnosis, treatment, prescription, rec_date
                )
            )

        elif choice == "5":
            print(process_billing())

        elif choice == "6":
            pid = input("Enter patient ID: ")
            e_type = input("Enter emergency type: ")
            severity = input("Enter severity level: ")
            print(manage_emergency_admission(pid, e_type, severity))

        elif choice == "7":
            med_id = input("Enter Medication ID: ")
            track_medication_inventory(med_id)

        elif choice == "8":
            pid = input("Enter Patient ID: ")
            assign_room(pid)

        elif choice == "9":
            pid = input("Enter Patient ID: ")
            calculate_treatment_cost(pid)

        elif choice == "10":
            pid = input("Enter patient ID: ").strip()
            r_type = input("Enter report type (e.g., Blood Test, X-Ray): ").strip()
            print(generate_patient_report(pid, r_type))

        elif choice == "11":
            print(analyze_hospital_efficiency())

        elif choice == "12":
            pid = input("Enter patient ID: ").strip()
            d_date = input("Enter discharge date (YYYY-MM-DD): ").strip()
            follow_up = input("Enter follow-up instructions: ").strip()
            print(manage_discharge_process(pid, d_date, follow_up))

        elif choice == "13":
            print("Exiting system.")
            break

        else:
            print("Invalid option. Please try again.")


main()
