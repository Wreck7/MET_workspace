# 8. Use a while loop to reverse a list manually (without using .reverse() or slicing).


numbers = [1,2,3,4,5,6,7]

reversed_numbers = []

while len(numbers) > 0:
    reversed_numbers.append(numbers.pop())

print(reversed_numbers)