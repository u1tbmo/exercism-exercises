def find_errors(search_list, value):
    if len(search_list) == 0:
        raise ValueError("value not in array")
    elif value < search_list[0] or value > search_list[-1]:
        raise ValueError("value not in array")

def find(search_list, value):
    find_errors(search_list, value)

    low = search_list[0]
    high = search_list[-1]
    middle = search_list[len(search_list) // 2]
    while low <= high:
        if value == middle:
            return search_list.index(middle)
        elif value < middle:
            high = search_list[search_list.index(middle) - 1]
            middle = search_list[(search_list.index(low) + search_list.index(high)) // 2]
        else:
            low = search_list[search_list.index(middle) + 1]
            middle = search_list[(search_list.index(low) + search_list.index(high)) // 2]
    if high < low:
        raise ValueError("value not in array")