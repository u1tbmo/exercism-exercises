"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_one, list_two):
    if list_one == list_two:
        return 2
    elif is_sublist(list_one, list_two):
        return 0
    elif is_sublist(list_two, list_one):
        return 1
    elif list_one != list_two:
        return 3

def is_sublist(a, b):
    if not a: # An empty list 'a' is a sublist of anything 'b'
        return True
    if not b: # An empty list 'b' cannot make 'a' a sublist
        return False
    for i in range(len(b) - len(a) + 1): # Iterate through b the maximum number of times that 'a' could be a sublist of 'b'
        if b[i:i+len(a)] == a: # If the slice of 'b' starting at index 'i' and ending at index 'i + len(a)' is equal to 'a', then 'a' is a sublist of 'b'
            return True
    return False