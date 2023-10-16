import string
import math

def cipher_text(plain_text):
    plain_text = plain_text.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").lower()
    plain_text_len = len(plain_text)

    row_len = int(math.sqrt(plain_text_len))
    col_len = row_len

    while row_len * col_len < plain_text_len:
        col_len += 1
        row_len = math.ceil(plain_text_len / col_len)

    crypto_square = []

    for i in range(row_len):
        crypto_square.append("")
        for j in range(col_len):
            try:
                crypto_square[i] += plain_text[i * col_len + j]
            except IndexError:
                crypto_square[i] += " "

    encoded = ""

    for i in range(col_len):
        for j in range(row_len):
            encoded += crypto_square[j][i]
        encoded += " "

    return encoded[:-1]

print(cipher_text("Chill out."))