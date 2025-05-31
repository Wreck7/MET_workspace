# Use input() to create a list of 5 numbers. Then, use a for-else loop to check if a specific number (entered by the user) is present. If found, print “Found”, else print “Not Found”.


numbers = []
v = 1
print("Enter 5 numbers:")
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

search_num = int(input("Enter the number to search for: "))

for num in numbers:
    if num == search_num:
        print("Found")
        break
else:
    print("Not Found")


