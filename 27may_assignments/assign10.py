# 9. Capitalize Names if Short (Using Tuple)
# Given tuple: ('sam', 'john', 'alex', 'bob'). If the name is 3 or fewer letters, print in uppercase. Else,
# capitalize.
# Expected Output: SAM, John, Alex, BOB


names = ('sam', 'john', 'alex', 'bob')

for i in names:
    if len(i) <=3:
        print(i.upper())
    else:
        print(i.capitalize())

