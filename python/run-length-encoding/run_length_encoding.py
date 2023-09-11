def decode_clean_list(char_list):
    decoded_list = []
    index = 0
    while index < len(char_list):
        current_char = char_list[index]
        try:
            next_char = char_list[index + 1]
        except IndexError:
            next_char = ""

        # check if the current character is a number
        if current_char.isnumeric():
            # if it is numeric, check if the next character is a number
            if next_char.isnumeric():
                decoded_list.append(current_char + next_char)
                index += 2 # skip the next character
                continue

            # if the next character is not numeric
            elif not next_char.isnumeric():
                decoded_list.append(current_char) 
            
            # increment the index
            index += 1

        # check if the current character is not a number
        elif not current_char.isnumeric():
            decoded_list.append(current_char)
            
            # increment the index
            index += 1

    return decoded_list

def decode(string):
    char_list = list(string)
    decoded_string = ""
    
    char_list = decode_clean_list(char_list)

    index = 0
    while index < len(char_list):
        current_char = char_list[index]
        try:
            next_char = char_list[index + 1]
        except IndexError:
            next_char = ""
        
        if current_char.isnumeric():
            decoded_string += next_char * int(current_char)
            index += 2
            continue
        elif not current_char.isnumeric():
            decoded_string += current_char
            index += 1
            continue

    return decoded_string

    

def encode(string):
    char_list = list(string)
    encoded_string = ""

    count = 1 # start from 1
    for index, element in enumerate(char_list):
        current_char = element
        try:
            next_char = char_list[index + 1]
        except IndexError:
            next_char = ""
        
        if current_char == next_char:
            count += 1
            continue
        elif current_char != next_char:
            if count == 1: # if the count is 1, don't add the count
                encoded_string += current_char
            else: 
                encoded_string += str(count) + current_char
            count = 1
            continue

    return encoded_string