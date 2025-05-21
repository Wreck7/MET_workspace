menu = {
    'idli' : 20,
    'dosa' : 30,
    'puri' : 25,
    'vada' : 35,
}

first_item = input('enter the first item: ')
first_count = int(input('enter the first count: '))
second_item = input('enter the second item: ')
second_count = int(input('enter the second count: '))

bill = 0

if first_item == 'idli':
    bill += menu['idli'] * first_count
elif first_item == 'dosa':
    bill += menu['dosa'] * first_count
elif first_item == 'puri':
    bill += menu['puri'] * first_count
elif first_item == 'vada':
    bill += menu['vada'] * first_count



if second_item == 'idli':
    bill += menu['idli'] * second_count
elif second_item == 'dosa':
    bill += menu['dosa'] * second_count
elif second_item == 'puri':
    bill += menu['puri'] * second_count
elif second_item == 'vada':
    bill += menu['vada'] * second_count


print(f'''
      item 1 : {first_item}    count: {first_count}
      item 2 : {second_item}   count: {second_count}
      Your total bill is: {bill}
Thank you for visiting our restaurant!
''')