#Assign 2
#Create a function called check_even_odd()
#It should take one parameter called 'number'
#It will print 'Even' if the number is even, if not print 'Odd'

number = int(input('enter a number please: '))

def check_even_odd(num):
    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'

checking = check_even_odd(number)

print(checking)