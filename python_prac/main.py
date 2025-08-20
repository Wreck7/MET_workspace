# question1
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


# 2) Palindrome Checker.!
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


# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):  # check up to sqrt(n)
#         if n % i == 0:
#             return False
#     return True

# num = int(input("Enter a number: "))
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")



# 8) Reverse a List
# ➤ Given a list, reverse it without using reverse().


# arr = [1,2,3,4,5,6]
# reversed_arr = []

# for i in arr:
#     reversed_arr.insert(0,i)
# print(reversed_arr)


# 9) Find Duplicates in a List
# ➤ Identify and print duplicate values from a list.


# arr = [1,2,1,3,4,5,3,6]
# seen = set()
# duplicates = set()

# for i in arr:
#     if i in seen:
#         duplicates.add(i)
#     else:
#         seen.add(i)
        
# print(duplicates)




# str = 'swiss'

# for i in str:
#     if str.count(i) == 1:
#         print(i)
#         break



# s = 'crypt'

# vowels = set('aeiou')

# def vowel_check(s):
#     for i in range(len(s)):
#         if s[i] in vowels:
#             return i
#     return -1

# first_index = vowel_check(s)
# if first_index == -1:
#     print(f'no vowels found!')
# else:
#     print(f'first vowel index {first_index}')



# s = 'education'

# arr = list(s)
# def moving_vowels(arr):
#     vowels = set('aeiou')
#     for i in arr:
#         if i in vowels:
#             arr.remove(i)
#             arr.append(i)
#     arr = ''.join(arr)
#     return arr

# print(moving_vowels(arr))




# s = 'mysecretpassword1234'

# masked = '*' * (len(s) - 4) + s[-4:]
# print(masked)



# s = 'python'
# staircase = '\n'.join(s)
# print(staircase)




# num = int(input("Enter a number: "))
# rev = 0

# while num != 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10

# print("Reversed number:", rev)



# string reversing 


# def reverse_sentence(sentence):
#     words = sentence.split()

#     def helper(index):
#         if index == len(words) - 1:
#             return words[index]
#         return helper(index + 1) + " " + words[index]

#     return helper(0)

# # Example usage
# sentence = input("Enter a sentence: ")
# reversed_sentence = reverse_sentence(sentence)
# print("Reversed sentence:", reversed_sentence)


# for i in range(11):
#     print(i)

# for i in range(11):
#     print(i)



#  javascript is way better than python

