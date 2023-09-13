def count_words(sentence):
    word_dict = {}

    # removes single quotation marks from beginning and end of sentence
    sentence = sentence.strip("'")
    # removes double quotation marks from beginning and end of sentence
    sentence = sentence.strip('"')

    for char in sentence:
        # replaces all punctuation with spaces excluding apostrophes and spaces
        if not char.isalnum() and char != "'" and char != " ":
            sentence = sentence.replace(char, " ")

    word_list = sentence.split(" ")

    # removes empty strings, spaces, quotation marks, and apostrophes from list
    while "" in word_list:
        word_list.remove("")
    while " " in word_list:
        word_list.remove(" ")
    while '"' in word_list:
        word_list.remove('"')
    while "'" in word_list:
        word_list.remove("'")
    
    # makes all words lowercase
    for word in word_list:
        word_list[word_list.index(word)] = word.lower()
    # removes quotation marks from beginning and end of words
    for word in word_list:
        word_list[word_list.index(word)] = word.strip('"')
    for word in word_list:
        word_list[word_list.index(word)] = word.strip("'")

    # for every occurrence of a word, add 1 to the count
    for word in word_list:
        if word not in word_dict:
            word_dict.update({word: 1})
        else:
            word_dict[word] += 1
    
    return word_dict