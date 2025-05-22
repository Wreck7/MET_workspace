# Assignment 6: 🧾 Order Summary (Dict of Dicts)
# 📘 Objective:
# Show price of an item from an order summary.
# ✅ Steps:
# 1. Create a dictionary like
# order = {
#    "item1": {"name": "Laptop", "price": 700},
#    "item2": {"name": "Mouse", "price": 20}
# }
# 2. Ask the user to enter an item key: ("item1" or "item2")
# 3. Use an if-elif-else block to:
# • Check which item was entered.
# • Print the item name and price.
# • If key is invalid, print: "Item not found."



order = {
   "item1": {"name": "Laptop", "price": 700},
   "item2": {"name": "Mouse", "price": 20}
}

user_item = input('enter an item key: ').lower()

first_key = list(order.keys())[0]
second_key = list(order.keys())[1]

if user_item == first_key:
    print(f'item name: {order["item1"]['name']}, item price: {order["item1"]['price']}')
elif user_item == second_key:
    print(f'item name: {order["item2"]['name']}, item price: {order["item2"]['price']}')
else:
    print('item not found!')


