from store import hospital_data

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