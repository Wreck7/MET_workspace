# 4. Print Squares of Numbers, Skip Multiples of 3
# Given numbers from 1 to 10, print their squares. Use continue to skip numbers divisible by 3.
# Expected Output: Squares of all numbers except 3, 6, 9

numbers = [1,2,3,4,5,6,7,8,9,10]

for i in numbers:
    if i % 3 == 0:
        continue
    else:
        print(i**2)
