#Assign 4
#Ask the user for a number
#Create a function called generate_table(number)
# It should take 'number' as param and print multiplication table from 1 to 10 for this number
#Call the function


def generate_table(number):
    print(f'''
{number} x 1 = {number*1}
{number} x 2 = {number*2}
{number} x 3 = {number*3}
{number} x 4 = {number*4}
{number} x 5 = {number*5}
{number} x 6 = {number*6}
{number} x 7 = {number*7}
{number} x 8 = {number*8}
{number} x 9 = {number*9}
{number} x 10 = {number*10}
''')
    
number = int(input('enter a number: '))

generate_table(number)

