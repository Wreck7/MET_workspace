# 1. Sum Even Numbers in a List
# Given a list of numbers: [1, 4, 7, 10, 13, 16]. Iterate through the list using a for loop. Sum only the
# even numbers. Print the total sum at the end.
# Expected Output: 30


arr = [1,2,3,4,5,6,7,8,9,10,11]

count = 0
for i in arr:
    if i % 2 == 0:
        count += i


print(count)