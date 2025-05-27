# 6. Multiply Dictionary Values if Key Starts with 'a'
# Given dictionary: {'apple': 2, 'banana': 3, 'apricot': 4, 'berry': 5}. Multiply values where keys start with
# 'a'.
# Expected Output: Product of values: 8

fruits = {'apple': 2, 'banana': 3, 'apricot': 4, 'berry': 5}

fruits_keys = list(fruits.keys())
# print(fruits_keys)

multi = 1

for i in fruits_keys:
    if i[0] == 'a':
        multi *= fruits[i]

print(multi)

