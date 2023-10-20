def egg_count(display_value):
    return count_ones(convert_to_binary(display_value))

def convert_to_binary(display_value):
    binary_value = ""

    while display_value > 0:
        binary_value += str(display_value % 2)
        display_value = (display_value // 2)

    return int(binary_value[::-1]) if binary_value != "" else 0

def count_ones(binary_value):
    count = 0
    for c in str(binary_value):
        if c == "1":
            count += 1
    return count