from store import hospital_data

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
            "shift_schedule": {
                "start_time": start_time,
                "end_time": end_time
            },
        }
        return f"\nStaff added successfully with ID: {staff_id}\n"
    return f"\nStaff ID: {staff_id} already exists.\n"
