# 3. Create a while-else loop that continues asking the user to enter even numbers. If the user enters an odd number, break the loop. In the else block, print “All even numbers”.


while True:
    even = int(input('enter an even number: '))
    if even % 2 != 0:
        print("You entered an odd number. Exiting loop.")
        break
else:
    print('all even numbers')


