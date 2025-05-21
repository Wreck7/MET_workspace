# Assignment 1: 🛒 Add Product to Cart (List of Dicts)
# 📘 Objective:
# Simulate adding a product to a shopping cart. Prevent duplicates.
# ✅ Steps:
# 1. Create a list with one product:
# cart = [{"id": 1, "name": "Shirt", "qty": 1}]
# 2. Ask the user:
# • Product ID (int)
# • Product name (str)
# 3. Create a dictionary from the user’s input.
# 4. Use an if statement to check if the id of the new product matches the one already in the cart.
# 5. If it exists, print: "Item already in cart."
# 6. If it doesn’t exist, append it to the list and print the updated cart.


cart = [{"id": 1, "name": "Shirt", "qty": 1}]

user_choice_pid = int(input('enter product id: '))
user_choice_pname = input('enter product name: ')

user_choice = {
    'id': user_choice_pid,
    'name': user_choice_pname,
    'qty': 1
}

if cart[0]['id'] == user_choice['id']:
    print('item already exist in cart')
else:
    cart.append(user_choice)
    print(cart)


