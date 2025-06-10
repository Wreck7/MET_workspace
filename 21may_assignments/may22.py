
# def one_to_three():
#     print(1)
#     print(2)
#     print(3)


# def three_to_seven():
#     print(3)
#     print(4)
#     print(5)
#     print(6)
#     print(7)


# def seven_to_ten():
#     print(7)
#     print(8)
#     print(9)
#     print(10)



# three_to_seven()
# one_to_three()
# seven_to_ten()



# def greet(lang, name):
#     if lang == "en":
#         print(f"Hello, {name}")
#     elif lang == "fr":
#         print(f"Bonjour, {name}")
#     else:
#         print(f"Hola, {name}")

# greet('en', 'vishwa')


# def greet(lang):
#     if lang == "en":
#         return "Hello"
#     elif lang == "fr":
#         return "Bonjour"
#     else:
#         return "Hola"

# print(greet('fr'), 'tejas')



data = [
    {
    'name': 'tejas',
    'age': 21
},
    {
    'name': 'karthik',
    'age': 19
}
]

def get_names(info):
    name_1 = info[0].get('name')
    name_2 = info[1].get('name')
    return [name_1, name_2]

def get_ages(info):
    age_1 = info[0].get('age')
    age_2 = info[1].get('age')
    return [age_1, age_2]


names = get_names(data)
ages = get_ages(data)
print(names, ages)
