ones_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5:'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
tens_dict = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6:'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
teens_dict = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14:'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18:'eighteen', 19: 'nineteen'}

def convert_to_word(number):
    if len(number) > 1: # remove leading zeros
        if number[0] == '0' and number[1] == '0' and number[2] == '0':
            return 'EMPTY GROUP'

        elif number[0] == '0' and number[1] == '0':
            number = number[2]

        elif number[0] == '0':
            number = number[1]

    word_bank = []

    # 3 digits
    if len(number) == 3:
        # get the digits
        first_digit = int(number[0])
        second_digit = int(number[1])
        third_digit = int(number[2])
        teens_digit = int(number[1:]) # handle special tens case

        # the first digit is the hundreds place (e.g. 100 => one hundred)
        if first_digit != 0:
            word_bank.append(ones_dict[first_digit])
            word_bank.append(' hundred ')

        # the second digit is the tens place, depending on the number, may be special case
        if second_digit == 1: # (e.g. 110 => one hundred ten, 111 => one hundred eleven etc.)
            word_bank.append(teens_dict[teens_digit])
        elif second_digit == 0 and third_digit == 0: # (e.g. 100 => one hundred, 200 => two hundred etc.)
            pass
        elif second_digit != 0 and third_digit == 0: # (e.g. 120 => one hundred twenty, 130 => one hundred thirty etc.)
            word_bank.append(tens_dict[second_digit])
        elif second_digit == 0: # (e.g. 103 => one hundred three, 206 => two hundred six etc.)
            word_bank.append(ones_dict[third_digit])
        else: # (e.g. 123 => one hundred twenty-three, 726 => seven hundred twenty-six etc.)
            word_bank.append(tens_dict[second_digit])
            word_bank.append('-')
            word_bank.append(ones_dict[third_digit])

    elif len(number) == 2:
        first_digit = int(number[0])
        second_digit = int(number[1])

        # the first digit is the tens place, depending on the number, may be special case
        if first_digit == 1: # (e.g. 10 => ten, 11 => eleven etc.)
            word_bank.append(teens_dict[int(number)])
        elif first_digit != 0 and second_digit == 0: # (e.g. 20 => twenty, 30 => thirty etc.)
            word_bank.append(tens_dict[first_digit])
        else: # (e.g. 23 => twenty-three, 76 => seventy-six etc.)
            word_bank.append(tens_dict[first_digit])
            word_bank.append('-')
            word_bank.append(ones_dict[second_digit])
    else: # len(number) == 1
        word_bank.append(ones_dict[int(number)]) # (e.g. 1 => one, 2 => two etc.)

    return ''.join(word_bank)
        
def say(number):
    # count the number of digits in the number
    digits = len(str(number))

    # check if number is out of range
    if number < 0:
        raise ValueError('input out of range')
    elif number > 999_999_999_999:
        raise ValueError('input out of range') 

    reversed_number_str = str(number)[::-1] # reverse to start from the ones place (e.g. 123456 => 654321)

    # split the number into groups of three digits then reverse the group itself
     # e.g. 654321 => 654, 321 => 456, 123
    split_number = [reversed_number_str[i:i+3][::-1] for i in range(0, len(reversed_number_str), 3)]
    split_number.reverse() # reverse back to original order (e.g. 456, 123 => 123, 456)

    word_list = []
    # for every hundred number group, convert it to its word form
    for number_group in split_number:
        word_list.append(convert_to_word(number_group))

    # check the number of elements in the word list and add the correct word after each group
    number_group_count = len(word_list)
    if number_group_count == 1:
        pass
    elif number_group_count == 2:
        word_list.insert(1, ' thousand ') # [000,thousand, 000]
    elif number_group_count == 3:
        word_list.insert(1, ' million ') # [000, million, 000, 000]
        word_list.insert(3, ' thousand ') # [000, million, 000, thousand, 000]
    elif number_group_count == 4:
        word_list.insert(1, ' billion ') # [000, billion, 000, 000, 000, 000]
        word_list.insert(3, ' million ') # [000, billion, 000, million, 000, 000]
        word_list.insert(5, ' thousand ') # [000, billion, 000, million, 000, thousand, 000]

    # create a new list with the wrong words removed and empty groups removed
    new_word_list = []
    current_index = 0
    while current_index < len(word_list):
        if word_list[current_index] == 'EMPTY GROUP':
            try:
                current_index += 2 # skips the empty group and the following word
            except IndexError:
                break
        else:
            new_word_list.append(word_list[current_index])
            current_index += 1

    # join the word list into a string
    word_form = ''.join(new_word_list).strip()
    return word_form