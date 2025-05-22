# Assignment 4: 🔐 Login System (Dict with Tuple Keys)
# 📘 Objective:
# Validate user login credentials.
# ✅ Steps:
# 1. Create a dictionary where keys are (username, password) tuples and values are roles:
# users = {("john", "1234"): "admin", ("alice", "abcd"): "editor"}

# 2. Ask the user:
# • Username (str)
# • Password (str)
# 3. Form a tuple from their input.
# 4. Check if the tuple exists in the dictionary using if.
# 5. If valid, print: "Welcome, <role>"
# 6. If invalid, print: "Invalid login."



users = {("john", "1234"): "admin", ("alice", "abcd"): "editor"}
user_username = input('enter username: ')
user_password = input('enter password: ')

user = (user_username, user_password)

if user in users:
    print(f'welcome, {users[user]}')
else:
    print('invalid login')
