from store import hospital_data

def schedule_appointment(
    patient_id, doctor_id, appointment_date, appointment_time, appointment_type
):
    if patient_id not in hospital_data["patients"]:
        return "\nInvalid patient ID.\n"
    if doctor_id not in hospital_data["staff"]:
        return "\nInvalid doctor ID.\n"

    for a in hospital_data["appointments"]:
        if (
            a["doctor_id"] == doctor_id
            and a["date"] == appointment_date
            and a["time"] == appointment_time
        ):
            return f"\nConflict: Doctor already has an appointment at {appointment_time} on {appointment_date}.\n"

    new_id = str(len(hospital_data["appointments"]) + 1)
    appointment = {
        "id": new_id,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": appointment_date,
        "time": appointment_time,
        "type": appointment_type,
    }
    hospital_data["appointments"].append(appointment)
    return f"\nAppointment scheduled successfully with ID {new_id}.\n"
