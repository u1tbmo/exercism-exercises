letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# index = "0123456789
# s_bet = "013579" (space between letters)

def rows(letter):
    # Initialize important variables
    diamond_list = []
    s_bet = "" # space between letters
    s_bef_aft = "" # space before and after letters (and middle spaces)

    # Find the index of the letter in the alphabet string
    letter_index = letters.find(letter)

    # A is a special case, return it in a list immediately
    if letter_index == 0:
        return [letter]
    
    # Calculate the maximum length of the middle string by computing the length of the space between the two letters
    s_bet_count = 1
    for i in range(1, letter_index):
        s_bet_count += 2
    s_bet = " " * s_bet_count

    # Append the middle string to the diamond list (f"{letter}{s_bet}{letter}")
    diamond_list.append(f"{letter}{s_bet}{letter}")

    # For each letter before the middle letter, subtract 2 from the s_bet_count, add 1 to the s_bef_aft_count, and append the string to the diamond list before and after (the end of the list) the middle string
    s_bef_aft_count = 0
    for i in range(letter_index, 0, -1):
        s_bef_aft_count += 1
        s_bef_aft = " " * s_bef_aft_count
        letter = letters[i - 1] # Get the letter before the middle letter

        # Once it reaches A
        if letter == "A":
            diamond_list.insert(0,f"{s_bef_aft}{letter}{s_bef_aft}")
            diamond_list.append(f"{s_bef_aft}{letter}{s_bef_aft}")

        # General cases
        else:
            s_bet_count -= 2
            s_bet = " " * s_bet_count
            diamond_list.insert(0, f"{s_bef_aft}{letter}{s_bet}{letter}{s_bef_aft}")
            diamond_list.append(f"{s_bef_aft}{letter}{s_bet}{letter}{s_bef_aft}")

    # Return the diamond list
    return diamond_list