color_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
value_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
tolerance_color_list = ['grey', 'violet', 'blue', 'green', 'brown', 'red', 'gold', 'silver']
tolerance_list = [0.05, 0.1, 0.25, 0.5, 1, 2, 5, 10]

def color_code(color):
    for index, c in enumerate(color_list):
        if color == c:
            return value_list[index]

def tolerance_code(tolerance):
    for index, t in enumerate(tolerance_color_list):
        if tolerance == t:
            return tolerance_list[index]
        
def value(colors):
    if len(colors) == 4:
        band_one, band_two, multiplier, *_ = colors
        return (color_code(band_one) * 10 + color_code(band_two)) * 10**color_code(multiplier)
    elif len(colors) == 5:
        band_one, band_two, band_three, multiplier, *_ = colors
        return (color_code(band_one) * 100 + color_code(band_two) * 10 + color_code(band_three)) * 10**color_code(multiplier)
    elif len(colors) < 4:
        if len(colors) == 1:
            return color_code(colors[0])
        elif len(colors) == 2: 
            return color_code(colors[0]) * 10 + color_code(colors[1])
        elif len(colors) == 3:
            return color_code(colors[0]) * 10 + color_code(colors[1]) + color_code(colors[2]) * 10**color_code(colors[2])
        
def label(colors):
    val = value(colors)
    if val < 1000:
        return str(val) + " ohms"
    elif val < 1000000 and str(val)[-3:] == '000':
        return str(val // 1000) + " kiloohms"
    elif val < 1000000:
        return str(val / 1000) + " kiloohms"
    elif val < 1000000000 and str(val)[-6:] == '000000':
        return str(val // 1000000) + " megaohms"
    elif val < 1000000000:
        return str(val / 1000000) + " megaohms"
    elif val < 1000000000000 and str(val)[-9:] == '000000000':
        return str(val // 1000000000) + " gigaohms"
    elif val < 1000000000000:
        return str(val / 1000000000) + " gigaohms"
    elif val < 1000000000000000 and str(val)[-12:] == '000000000000':
        return str(val // 1000000000000) + " teraohms"
    else:
        return str(val / 1000000000000) + " teraohms"

def resistor_label(colors):
    last_color = colors[-1]
    if len(colors) == 4:
        return f"{label(colors)} ±{tolerance_code(last_color)}%"
    elif len(colors) == 5:
        return f"{label(colors)} ±{tolerance_code(last_color)}%"
    elif len(colors) < 4:
        return f"{label(colors)}"
    
