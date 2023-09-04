color_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
value_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def color_code(color):
    for index, c in enumerate(color_list):
        if color == c:
            return value_list[index]
        
def value(colors):
    band_one, band_two, multiplier, *_ = colors
    return (color_code(band_one) * 10 + color_code(band_two)) * 10**color_code(multiplier) # type: ignore

def label(colors):
    value_length = len(str(value(colors)))
    if value_length == 4 or value_length == 5 or value_length == 6:
        return str(value(colors))[:-3] + " kiloohms"
    elif value_length == 7 or value_length == 8 or value_length == 9:
        return str(value(colors))[:-6] + " megaohms"
    elif value_length == 10 or value_length == 11 or value_length == 12:
        return str(value(colors))[:-9] + " gigaohms"
    else:
        return str(value(colors)) + " ohms"
