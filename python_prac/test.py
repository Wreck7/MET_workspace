''''1. Maximum & Classification Combo
Write a function that takes three integers and returns the maximum of them. Also determine if the
maximum is even or odd and whether it is positive, negative, or zero. Return a single formatted
string.
'''


# def checking_func(a, b, c):
#     largest = 0
#     if a > b and a > c:
#         largest = a
#     elif b > a and b > c:
#         largest = b
#     else:
#         largest = c
    
#     even_or_odd = ''
#     if largest % 2 == 0:
#         even_or_odd = "an Even"
#     else:
#         even_or_odd = 'a Odd'
        
#     pos_neg_zero = ''
#     if largest > 0:
#         pos_neg_zero = 'Positive'
#     elif largest < 0:
#         pos_neg_zero = 'Negative'
#     else:
#         pos_neg_zero = 'Zero'
    
#     return f'''{largest} is maximum of {a,b,c}, {largest} is {even_or_odd} number and its a {pos_neg_zero} number'''

# result = checking_func(5,-7,2)
# print(result)


'''2. Character Classifier
Given a single character input, determine and return whether it is:
- Uppercase Vowel
- Lowercase Vowel
- Uppercase Consonant
- Lowercase Consonant
- Digit
- Special Character'''


# def checking_char(c):
#     u_vowels = set('AEIOU')
#     l_vowels = set('aeiou')
#     statement = ''
    
#     if s.isalpha() and s in u_vowels:
#         statement = 'Uppercase Vowel'
#     elif s.isalpha() and s in l_vowels:
#         statement = 'Lowercase Vowel'
#     elif s.isalpha() and s not in u_vowels:
#         statement = 'Uppercase Consonant'
#     elif s.isalpha() and s not in l_vowels:
#         statement = 'Lowercase Consonant'
#     elif s.isdigit():
#         statement = 'Digit'
#     else:
#         statement = 'Special Character'
#     return f'its a {statement}'

# s = input('enter a single character: ')
# result = checking_char(s)
# print(result)



'''3. Pyramid / Triangle Pattern
Write a program to print a pyramid or triangle pattern using stars (*) with the given number of rows.
'''

# def printing_tri(n):
#     for i in range(1, n+1):
#         print("*"*i)

# row = int(input('enter a number of rows: '))
# result = printing_tri(row)


'''4. Even Numbers Using Recursion
Write a recursive function that prints all even numbers from 1 to N.'''


# def print_even(n, current=2):
#     if current > n:
#         return
#     print(current)
#     print_even(n, current + 2)

# num = int(input("Enter a number: "))
# print_even(num)



'''6. Sum of Natural Numbers
Write a program to calculate the sum of the first N natural numbers.
'''

# def sum_nums(num):
#     total = 0
#     for i in range(1, num+1):
#         total += i
#     return total

# num = int(input('enter a number: '))
# print(sum_nums(num))


'''7. Palindrome & Anagram Checker
Write two functions:
- One to check if a word is a palindrome (same forward and backward).
- Another to check if two words are anagrams of each other (same letters, different order)'''

# def checking_palindrome():
#     word = input('enter a word to check palindrome: ')
#     reversed_word = word[::-1]
#     if reversed_word == word:
#         print('yeah, its a palindrome!')
#     else:
#         print("nope, it isn't a palindrome!")

# def checking_anagram():
#     word1 = input('enter a word to check anagram: ')
#     word2 = input('enter a word to check anagram: ')
#     w1 = list(sorted(word1))
#     w2 = list(sorted(word2))
#     if w1 == w2:
#         print('yes, its an anagram!')
#     else:
#         print('no, its not an anagram!')

# checking_palindrome()
# checking_anagram()