person = {
    "name": 'joy',
    'age': 45,
    'hobbies': ['dancing', 'swimming', 'reading']
}

for k in person:
    if k == 'hobbies':
        myhobbies = person['hobbies']
        for i in myhobbies:
            print(i)


