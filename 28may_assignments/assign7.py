# 7. Ask the user to input 5 names using input() and store them in a list. Then, use a for-else loop to check if a specific name exists.


names = []

for i in range(5):
    name = input('enter a name: ')
    names.append(name)

search_name = input('enter a name to search: ')

for name in names:
    if search_name == name:
        print(f'yes {search_name} exist in the list')
        break
else:
    print(f"no {search_name} doesn't exist in the list")


