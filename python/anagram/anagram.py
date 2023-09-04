import string

lowercase_dict = {char: 0 for char in string.ascii_lowercase}

def find_anagrams(word, candidates):
    valid_candidates = []
    for candidate in candidates:
        if word.lower() == candidate.lower() or len(word) != len(candidate):
            continue

        word_letters = letters_in_word(word)
        candidate_letters = letters_in_word(candidate)

        if word_letters == candidate_letters:
            valid_candidates.append(candidate)
    return valid_candidates

def letters_in_word(word):
    letters_dict = lowercase_dict.copy()
    for letter in word.lower():
        if letter in letters_dict:
            letters_dict[letter] += 1
    return letters_dict