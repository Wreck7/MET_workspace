# s = "hey, good morning!?"

# user_input = input('enter any character: ')
# try:
#     print(s.replace(user_input, ""))
# except SyntaxError as e:
#     print(f"no character {user_input} found")


vowels = set("aeiou")

s = input('enter a sentence: ')

vowel_count = 0
consonant_count = 0
digit_count = 0
space_count = 0

for i in s:
    if i.lower() in vowels:
        vowel_count += 1
    elif i == " ":
        space_count += 1
    elif i.isdigit():
        digit_count +=1
    else:
        consonant_count += 1
        
print(f'vowels: {vowel_count}, consonants: {consonant_count}, digits: {digit_count}, spaces: {space_count}')

