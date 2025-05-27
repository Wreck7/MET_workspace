# 7. Print Unique Words Ignoring Stop Words (Using Set)
# Given list: ['python', 'code', 'loop', 'if', 'python', 'else', 'if']. Print unique words excluding stop words:
# {'if', 'else'}.
# Expected Output: Unique non-stop words: {'python', 'code', 'loop'}


# Given list of words
words = ['python', 'code', 'loop', 'if', 'python', 'else', 'if']

# Stop words to exclude
stop_words = {'if', 'else'}

# Use set to get unique words, then subtract stop words
unique_non_stop_words = set(words) - stop_words

# Print result
print("Unique non-stop words:", unique_non_stop_words)





