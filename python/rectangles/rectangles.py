def rectangles(strings: list[str]) -> int:
    qty = 0

    if not strings:
        return 0

    width = len(strings[0])
    height = len(strings)

    for row_index, line0 in enumerate(strings):
        for li, char0 in enumerate(line0):
            if char0 == '+':
                for ri, char1 in enumerate(line0[li+1:width]):
                    if char1 == '+':
                        for line1 in strings[row_index+1:height]:
                            char2 = line1[li]
                            char3 = line1[li+ri+1]
                            if char2 == '+' and char3 == '+':
                                if all(char in '+-' for char in line1[li:li+ri+1]):
                                    qty += 1
                            elif char2 not in '+|' or char3 not in '+|':
                                break
                    elif char1 == '-':
                        continue
                    else:
                        break

    return qty

print(
    rectangles(
        [
            "+-+ +-+",
            "| | | |",
            "+-+-+-+",
            "  | |  ",
            "+-+-+-+",
            "| | | |",
            "+-+ +-+",
        ]
    )
)
