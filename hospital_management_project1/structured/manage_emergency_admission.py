from store import hospital_data

def manage_emergency_admission(patient_id, emergency_type, severity_level):
    if patient_id in hospital_data["patients"]:
        emergency = {
            "patient_id": patient_id,
            "type": emergency_type,
            "severity": severity_level,
        }
        hospital_data["emergency_cases"].append(emergency)
        return f"\nEmergency case recorded. Patient ID: {patient_id}\n"
    else:
        return "Patient ID not found."
