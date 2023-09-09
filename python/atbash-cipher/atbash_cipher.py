plain_alphabet = "abcdefghijklmnopqrstuvwxyz"
ciphered_alphabet = "zyxwvutsrqponmlkjihgfedcba"

def encode(plain_text):
    to_encode = str.maketrans(plain_alphabet, ciphered_alphabet)

    dummy_text = plain_text
    for letter in plain_text:
        if letter == " " or letter == "," or letter == "." or letter == "!":
            dummy_text = dummy_text.replace(letter, "")
        else:
            continue

    plain_text = dummy_text.lower().replace(" ", "").translate(to_encode)

    count = 5
    for i in range(1, len(plain_text) + 1 + len(plain_text) % 5):
        if i % count == 0:
            plain_text = plain_text[:i] + " " + plain_text[i:]
            count += 6
            
    return plain_text.strip()


def decode(ciphered_text):
    to_decode = str.maketrans(ciphered_alphabet, plain_alphabet)
    return ciphered_text.lower().replace(" ", "").translate(to_decode)