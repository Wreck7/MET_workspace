from store import hospital_data

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
