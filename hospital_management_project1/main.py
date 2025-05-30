patient_database = {}

# generating a unique patient id 
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def generate_id():
    id_digits = []
    for i in range(5):
        index = (i*3+2) % len(numbers)
        id_digits.append(str(numbers[index]))
    return f'P{''.join(id_digits)}'

uni_id = generate_id()
# print(f'generated id: {uni_id}')

# user personal info
def personal_info_inputs():
    name = input('enter your name: ').title()
    age = input('enter your age: ')
    gender = input('enter your gender: ').capitalize()
    blood_group = input('enter your blood group: ').upper()
    insurance_name = input('enter your insurance name: ').title()
    insurance_id = input('enter your insurance policy id: ')

    insurance_info = {
    "insurance_name": insurance_name,
    'insurance_id': insurance_id
    }

    return {
        'name': name,
        'age': age,
        'gender': gender,
        'blood_group': blood_group,
        'insurance_name': insurance_name,
        'insurance_id': insurance_id
    }, insurance_info

# user_info,insurance_info = personal_info_inputs()
# print(user_info)
# print(insurance_info)


# def register_patient(patient_id, personal_info, insurance_info): #  (medical_history) missed this cauz how can i say this
#     patient_database.update({
#         patient_id: personal_info
#     })

#     return f'''
#     === PATIENT DASHBOARD ===
#     Patient: {personal_info.get('name')} (ID: {patient_id})
#     Age: {personal_info.get('age')} | Gender: {personal_info.get('age')} | Blood Type: {personal_info.get('blood_group')}
#     Insurance: {personal_info.get('insurance_name')} (Policy: {personal_info.get('insurance_id')})
#     '''

# done = register_patient(uni_id,user_info,insurance_info)
# print(done)

