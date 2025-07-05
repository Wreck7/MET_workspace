# animals = ['cat', 'dog', 'monkey', 'cow']

# for i in range(len(animals)):
#     current = animals[i]
#     next_animal = animals[(i + 1) % len(animals)]  # wraps around
#     next_two = next_animal[:2]
#     print(current + next_two)



# 1) Sum of Digits
# ➤ Input a number and print the sum of its digits.
# Example: 123 → 6


# number = input('enter a number: ')

# count = 0
# for i in range(len(number)):
#     count += int(number[i])
# print(count)


# 2) Palindrome Checker
# ➤ Check if a string is a palindrome (reads the same backward).
# Example: "madam" → YES


# user_input = input('enter a word: ')

# reversed_word = user_input[::-1]
# if user_input == reversed_word:
#     print(f'{user_input} -> YES')
# else:
#     print(f'{user_input} -> NO')
    


# 3) Count Vowels in a String
# ➤ Given a string, count how many vowels it contains.


# user_input = input('enter a word: ').lower()

# vowels = ['a', 'e', 'i', 'o', 'u']
# count = 0

# for i in range(len(user_input)):
#     if user_input[i] in vowels:
#         count += 1

# print(count)


# 4) Factorial Finder
# ➤ Given n, print n! using a loop or recursion.

# number = int(input('enter a number: '))
# factorial = 1

# for i in range(1, number+1):
#     factorial *= i

# print(factorial)



# 5) Fibonacci Series
# ➤ Print the first n terms of the Fibonacci sequence.


# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         print(a)
#         a, b = b, a+b
        
# fibonacci(10)


# 6) Largest of Three Numbers
# ➤ Take three integers as input and print the largest.

# number1 = int(input('enter a number: '))
# number2 = int(input('enter a number: '))
# number3 = int(input('enter a number: '))
# large_number = 0

# if number1 > number2 and number1 > number3:
#     large_number = number1
# elif number2 > number1 and number2 > number3:
#     large_number = number2
# else:
#     large_number = number3
    
# print(large_number)


# 7) Find Prime Numbers
# ➤ Check if a number is prime, or print all primes up to n.



