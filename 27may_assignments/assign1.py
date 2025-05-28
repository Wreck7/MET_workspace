person = {
    "name": 'joy',
    'age': 45,
    'hobbies': ['dancing', 'swimming', 'reading']
}

for k in person:
    if k == 'hobbies':
        my_hobbies = person['hobbies']
        for i in my_hobbies:
            print(i)


