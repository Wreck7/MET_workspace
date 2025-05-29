# 6. Create a dictionary where keys are fruits and values are prices. Use dictionary methods to:
# • Add a new fruit
# • Update the price of an existing fruit
# • Delete a fruit
# • Display all fruits with prices


fruits = {
    'apple': 200,
    'mango': 60,
    'kiwi': 100
}

fruits.update({'banana': 45, 'apple': 120})

fruits.pop('kiwi')

print(fruits)

