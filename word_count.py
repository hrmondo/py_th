# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.


1) OK

from collections import Counter

def word_count(string):
    count_dict = Counter(string.lower().split())
    return count_dict



2) ??NOT tried

def word_count(string):
    new_dict = {}
    new_string = string.lower().split()
    for word in new_string:
        if word not in new_dict:
            new_dict.update({word:new_string.count(word)})
    return new_dict




