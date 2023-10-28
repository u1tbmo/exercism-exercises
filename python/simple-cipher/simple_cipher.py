import secrets
import string

alphabet = string.ascii_lowercase

class Cipher:
    def __init__(self, key=None):
        self.key = key.lower() if key is not None else self.generate_key()
        self.numeric_key = [alphabet.index(char) for char in self.key]

    def encode(self, text):
        encoded = ""
        for index, char in enumerate(text):
            shift_val = self.numeric_key[index % len(self.numeric_key)]
            encoded += self.rotate(char, shift_val)
        return encoded

    def decode(self, text):
        decoded = ""
        for index, char in enumerate(text):
            shift_val = (self.numeric_key[index % len(self.numeric_key)]) * -1
            decoded += self.rotate(char, shift_val)
        return decoded

    def rotate(self, text, key):
        cipher = alphabet[key:] + alphabet[:key]
        return text.translate(str.maketrans(alphabet, cipher))
    
    @staticmethod
    def generate_key():
        return ''.join(secrets.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(100))