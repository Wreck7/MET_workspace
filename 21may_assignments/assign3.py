# Assignment 3: 📍 Save Location (List of Tuples)
# 📘 Objective:
# Store unique GPS coordinates.
# ✅ Steps:
# 1. Create a list:
# locations = [(12.9716, 77.5946)]
# 2. Ask the user to input:
# • Latitude (float)
# • Longitude (float)
# 3. Combine them into a tuple.
# 4. Check using if whether this tuple already exists in the list.
# 5. If yes, print: "Location already exists."
# 6. If no, append the tuple and print the updated list.


locations = [(12.9716, 77.5946)]

user_latitude = float(input('enter latitude: '))
user_longitude = float(input('enter longitude: '))
user_location = (user_latitude, user_longitude)


if user_location[0] in locations[0][0] and user_location[1] in locations[0][1]:
    print('location already exists')
else:
    locations.append(user_location)
    print(f'updated list of locations is: {locations}')






