from register_patient import register_patient
from store import hospital_data


def registration():
    patient_id = f"{len(hospital_data['patients'])+1}"
    name = input("Enter patient name: ").title()
    age = input("Enter age: ")
    gender = input("Enter gender: ").capitalize()
    medical_history = input("Enter medical history (comma-separated): ").title().split(",")
    blood_group = input("Enter your blood group: ").upper()
    insurance_name = input("Enter insurance provider: ").title()
    insurance_id = input("Enter insurance id: ").upper()
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
