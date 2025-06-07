from store import hospital_data


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