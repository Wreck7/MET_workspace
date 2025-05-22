# Assign 1
# Create 4 functions called add, subtract, multiply, divide
# Each function should print the result of the operation
# Ask the user to enter two numbers and the operation (+, -, *, /)
# Call the relavent function based on user input


def add(num1, num2):
    print(num1 + num2)

def sub(num1, num2):
    print(num1 - num2)

def multi(num1, num2):
    print(num1 * num2)

def divide(num1, num2):
    print(num1 // num2)

num1 = int(input('enter a number: '))
num2 = int(input('enter another number: '))

operation = input('enter a operation to perform: ')

if operation == '+':
    add(num1,num2)
elif operation == '-':
    sub(num1,num2)
elif operation == '*':
    multi(num1,num2)
elif operation == '//' or operation == '/':
    divide(num1,num2)
else:
    print(f"{operation} this operation doesn't")
