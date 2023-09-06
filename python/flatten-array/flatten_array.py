def flatten(iterable):
    clean_iterable = []
    result = []

    list_is_not_flat = any(isinstance(element, list) for element in iterable)

    while list_is_not_flat:
        for element in iterable:
            if isinstance(element, list):
                result.extend(element)
            else:
                result.append(element)
        iterable = result
        list_is_not_flat = any(isinstance(element, list) for element in iterable)
        result = []

    for item in iterable:
        if item == None:
            continue
        else:
            clean_iterable.append(item)

    iterable = clean_iterable

    return iterable

flatten([0, 2, [[2, 3], 8, [[100]], None, [[None]]], -2])