def rotate(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher = alphabet[key:] + alphabet[:key]
    return text.translate(str.maketrans(alphabet + alphabet.upper(), cipher + cipher.upper()))
    