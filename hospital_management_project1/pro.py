# def register_patient(patient_id, personal_info, medical_history, insurance_info
"""
=== PATIENT DASHBOARD ===
Patient: Rajesh Kumar (ID: P12345)
Age: 45 | Gender: Male | Blood Type: B+
Insurance: Star Health (Policy: SH789456
"""

def register_patient(patient_id, personal_info, medical_history, insurance_info):
    pass

def add_medical_staff(staff_id, name, specialization):  # shift_schedule, contact_info):
    medical_staff_list= []
    medical_staff_dict = {
        'staff_id' : staff_id,
        'name' : name,
        'specialization' : specialization
    }
    medical_staff_list.append()
    return medical_staff_dict


print("Welcome to Hospital Management System with Patient Care")
print("select the task, enter the number of task")
print(
    "register_patient- 1 \n"
    'add_medical_staff- 2 \n'
    'schedule_appointment-3 \n'
    'create_medical_record- 4 \n'
    "process_billing-5 \n"
)
choice = int(input("Enter your task number: "))
if choice == 2:
    print("h")
    staff_id = input("enter staff id: ")
    name_staff = input("enter staff name: ")
    specialization_staff = input("enter specialization: ")
    print(add_medical_staff(staff_id, name_staff, specialization_staff))