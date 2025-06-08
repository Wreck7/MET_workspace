from store import hospital_data
from registration import registration


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
