import requests

related_word = input('Enter a word that you want and get related words: ')

letter_input = input('Enter a letter to get a corresponding word: ')

no_of_words = input("Enter how many words you want:")

res = requests.get(f"https://api.datamuse.com/words?ml={related_word}&sp={letter_input}*&max={no_of_words}")

content = res.json()
for i in range(len(content)):
    print(content[i]["word"])
