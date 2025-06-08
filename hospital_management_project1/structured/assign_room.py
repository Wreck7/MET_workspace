from store import hospital_data

def assign_room(patient_id):
    # First check if patient exists in hospital registration
    if patient_id not in hospital_data["patients"]:
        print(f"\nPatient '{patient_id}' is not registered in the hospital system.\n")
        return
    
    # Check if patient is already assigned to a room
    for room_num, info in hospital_data["room_assignments"].items():
        if info["patient"] == patient_id:
            print(f"\nPatient '{patient_id}' is already assigned to room {room_num}.\n")
            break
    else:
        # Patient is registered and not assigned, proceed with room assignment
        patient_name = hospital_data["patients"][patient_id]['name']
        print(f"\nAssigning room for patient: {patient_name} (ID: {patient_id})")
        
        room_type = input("Enter Room Type (Private/Shared): ")
        admission_date = input("Enter Admission Date (YYYY-MM-DD): ")
        expected_duration = input("Enter Expected Duration (e.g., 3 days): ")
        room_number = input("Enter Room Number (e.g., 101A): ")
        
        # Check if the requested room exists and is available
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