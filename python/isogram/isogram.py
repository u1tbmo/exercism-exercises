def is_isogram(sentence):
    # Check for special characters
    # https://stackoverflow.com/a/5843560
    stripped_sentence = ''.join(letter for letter in sentence if letter.isalnum())
    return not (len(stripped_sentence.lower()) > len(set(stripped_sentence.lower())))