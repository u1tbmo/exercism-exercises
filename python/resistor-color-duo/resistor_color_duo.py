color_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
value_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def value(colors):
    band_one, band_two, *_ = colors
    return color_code(band_one) * 10 + color_code(band_two)

def color_code(color):
    for index, c in enumerate(color_list):
        if color == c:
            return value_list[index]