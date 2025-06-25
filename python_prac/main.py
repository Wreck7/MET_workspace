animals = ['cat', 'dog', 'monkey', 'cow', 'mahi']

for i in range(len(animals)):
    current = animals[i]
    next_animal = animals[(i + 1) % len(animals)]  # wraps around
    next_two = next_animal[:2]
    print(current + next_two)
