# 7. Print Unique Words Ignoring Stop Words (Using Set)
# Given list: ['python', 'code', 'loop', 'if', 'python', 'else', 'if']. Print unique words excluding stop words:
# {'if', 'else'}.
# Expected Output: Unique non-stop words: {'python', 'code', 'loop'}



words = ['python', 'code', 'loop', 'if', 'python', 'else', 'if']

stop_words = {'if', 'else'}

unique_non_stop_words = set(words) - stop_words

print("Unique non-stop words:", unique_non_stop_words)





