from store import hospital_data

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
                "insurance_info": {
                "provider": insurance_name,
                "id": insurance_id
            },
        }
        return f"""
=== PATIENT DASHBOARD ===
Patient: {name} (ID: {patient_id})
Age: {age} | Gender: {gender} | Blood Type: {blood_group}
Insurance: {insurance_name} (Policy: {insurance_id})
"""

