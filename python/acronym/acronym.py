import re

def abbreviate(words):
    words = words.replace("'", "")
    words = re.sub(r"[^a-zA-Z0-9\-]", " ", words)
    words = words.replace("-", " ")

    acronym = ''
    word_list = words.split()
    for word in word_list:
        acronym += word[0].upper()
    return acronym

