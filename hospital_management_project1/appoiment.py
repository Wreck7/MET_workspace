# scheduling appointment here

def appointment_inputs():
    appointment_date = input('enter the date of appointment(dd-mm-yyyy/hh:mm): ')
    appointment_type = input('enter appointment type: ')
    return appointment_date, appointment_type

appointment_date, appointment_type = appointment_inputs()
# print(appointment_type)

appointments = []

def schedule_appointment(patient_id, doctor_id, appointment_date, appointment_type):
    for i in appointments:
        if i['doctor_id'] == doctor_id and i['appointment_date'] == appointment_date:
            return {"error": "Doctor is not available at the selected time."}
        
    appointment = {
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "appointment_date": appointment_date,
        "appointment_type": appointment_type
    }
    appointments.append(appointment)
    # return {"success": True, "appointment": appointment}
    return f'''
    === Appointment successful ===
    patient id: {appointment["patient_id"]} | doctor id: {appointment["doctor_id"]}
    appointment date: {appointment["appointment_date"]} | appointment type: {appointment["appointment_type"]}
    '''

done_appointment = schedule_appointment(uni_id, 'D123', appointment_date, appointment_type)
print(done_appointment)
