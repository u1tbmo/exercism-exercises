vowel_sounds = ["a", "e", "i", "o", "u", "xr", "yt"]

def translate(word):
    is_phrase = False
    for letter in word:
        if letter.isspace():
            is_phrase = True
            break

    if is_phrase:
        words = word.split()  # Split the input phrase into individual words
        translated_words = []

        for word in words:
            translated_word = translate(word)  # Translate each word
            translated_words.append(translated_word)

        translated_phrase = " ".join(translated_words)  # Join the translated words back into a phrase
        return translated_phrase
    
    else:
        # * Rule 1: (e.g. "xray" -> "xrayay", "yttria" -> "yttriaay")
        # Check if the word begins with a vowel sound by checking if the sliced word up to the second letter contains a vowel sound.
        if word[:2] in vowel_sounds:
            return word + "ay"

        # * Rule 2: (e.g. "chair" -> "airchay")
        # * Rule 3: (e.g. "square" -> "aresquay")
        # * Rule 4: (e.g. "rhythm" -> "ythmrhay", "my" -> "ymay").
        # Iterate through the sliced word up to the third letter and count any consonant sounds.
        # The count will be the length of the consonant sounds.
        count = 0
        for letter in word[:3]:
            # Check y condition first because it is a special case. Y after a consonant is a vowel sound.
            if word[0] == "y": # Treat y as a consonant sound if it is the first letter.
                count += 1
            if count <= 2 and letter == "y" and word[count - 1] not in vowel_sounds: # Treat y as a vowel sound if the previous letter is a consonant sound.
                break
            elif count <= 2 and letter not in vowel_sounds: # Check if the letter is a consonant sound.
                count += 1
            elif count <= 2 and letter == "u" and word[count - 1] == "q": # Treat "qu" as a consonant sound.
                count += 1
            else: # If the letter is a vowel sound.
                break
        return word[count:] + word[:count] + "ay" # Return the word with the consonant sounds moved to the end and "ay" appended.
    