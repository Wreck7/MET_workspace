# 8. Check if Any Number is a Perfect Square
# Given: [10, 25, 36, 40]. Print the first number that is a perfect square. Stop after finding it.
# Expected Output: 25 is a perfect square


integers = [1,2,3,4,5,6,7,8,9]

numbers = [10, 25, 36, 40]

integers_powers = []

for i in integers:
    integers_powers.append(i**2)

for i in numbers:
    if i in integers_powers:
        print(f'{i} is a perfect square')
        break
