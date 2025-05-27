# Find the First Negative Number in a Tuple
# Given a tuple: (3, 5, 9, -2, 6, -7), iterate and find the first negative number. Use break to stop when
# found.
# Expected Output: First negative number: -2


numbers = (3, 5, 9, -2, 6, -7)

for i in numbers:
    if i < 0:
        print(i)
        break
