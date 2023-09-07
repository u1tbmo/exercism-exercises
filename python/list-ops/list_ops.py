def append(list1, list2):
    for item in list2:
        list1.append(item)
    return list1


def concat(lists):
    concat_list = []
    for sublist in lists:
        for item in sublist:
            concat_list.append(item)
    return concat_list


def filter(function, list):
    filtered_list = []
    for element in list:
        if function(element):
            filtered_list.append(element)
    return filtered_list


def length(list):
    return len(list)


def map(function, list):
    mapped_list = []
    for element in list:
        mapped_list.append(function(element))
    return mapped_list


def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)
    return initial


def foldr(function, list, initial):
    for item in reverse(list):
        initial = function(initial, item)
    return initial


def reverse(list):
    return list[::-1]
