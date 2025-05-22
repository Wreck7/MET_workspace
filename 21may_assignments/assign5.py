# Assignment 5: 🏷️ Tag Manager (Set of Strings)
# 📘 Objective:
# Track unique tags on a blog post.
# ✅ Steps:
# 1. Create a set of tags:
# tags = {"python", "fastapi", "backend"}
# 2. Ask the user to input a new tag.
# 3. Use if to check if it exists in the set.
# 4. If it does, print: "Tag already exists."
# 5. If not, add it using add() and print the updated set


tags = {"python", "fastapi", "backend"}

user_tag = input('enter a new tag: ')

if user_tag in tags:
    print('tag already exists!')
else:
    tags.add(user_tag)
    print(f'updated set of tags are: {tags}')




