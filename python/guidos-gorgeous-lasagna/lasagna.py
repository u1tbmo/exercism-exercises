"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_baked_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return 40 - elapsed_baked_time

def preparation_time_in_minutes(layers):
    """Calculate the bake time remaining.

    :param layers: int - number of layers to prepare for the lasagna.
    :return: int - amount of time to prepare the lasagna for baking (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the number of layers needed to prepare the lasagna as an argument and returns the amount of time needed to prepare based on `PREPARATION_TIME`.
    """
    return layers * PREPARATION_TIME

def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return preparation_time_in_minutes(layers) + elapsed_bake_time
