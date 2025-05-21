# Assignment 2: 📂 Product Categories (Dict of Lists)
# 📘 Objective:
# Display available products in a given category.
# Steps:
# 1. Create a dictionary:
# categories = {
#    "clothes": ["shirt", "jeans"],
#    "electronics": ["phone", "charger"]
# }
# Ask the user to input a category name.
# 3. Use an if statement to check if the entered category exists in the dictionary.
# 4. If it exists, print the list of products.
# 5. If not, print "Invalid category."


categories = {
   "clothes": ["shirt", "jeans"],
   "electronics": ["phone", "charger"]
}

user_choice_category = input('enter a category name: ')


if user_choice_category in categories:
    print(f'available products in {user_choice_category} category: {categories[user_choice_category]}')
else:
    print('Invalid category')
