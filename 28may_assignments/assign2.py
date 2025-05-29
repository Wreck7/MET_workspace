# 2. Write a while loop that keeps asking the user to enter numbers until the total reaches or exceeds 100. Display how many numbers were entered.


total = 0

count = 0
while total <= 100:
    user_input = int(input('enter a number: '))
    total += user_input
    count += 1

print(f'user entered numbers {count} times')