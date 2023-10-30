number_dict = {
    10: "ten",
    9: "nine",
    8: "eight",
    7: "seven",
    6: "six",
    5: "five",
    4: "four",
    3: "three",
    2: "two",
    1: "one",
    0: "no",
}


def recite(start, take=1):

    def bottle_phrase(num):
        if num != 1:
            return f"{number_dict[i].capitalize()} green bottles hanging on the wall,"
        else:
            return f"{number_dict[i].capitalize()} green bottle hanging on the wall,"


    verse_list = []
    for i in range(start, start - take, -1):
        verse_list.extend([bottle_phrase(i)] * 2)

        verse_list.append("And if one green bottle should accidentally fall,")

        if i - 1 == 1:
            verse_list.append(f"There'll be {number_dict[i-1]} green bottle hanging on the wall.")
        else:
            verse_list.append(f"There'll be {number_dict[i-1]} green bottles hanging on the wall.")

        if take != 1 and i != start - take + 1:
            verse_list.append("")

    return verse_list
        
