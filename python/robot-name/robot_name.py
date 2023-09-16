import random

CACHE = set()
CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMS = '0123456789'

# generates a 5 character name (e.g. AB123)
def name_generator():
        generated_name = ''

        for i in range(2):
            generated_name += random.choice(CHARS)
        for i in range(3):
            generated_name += random.choice(NUMS)
        return generated_name

# generates a name and checks if it's in the cache
def initialize_name():
    name = name_generator()
    if name not in CACHE:
        CACHE.add(name)
        return name
    else:
        name = initialize_name()
    return name

# Robot class
class Robot:
    # initialize the robot with a name
    def __init__(self):
        self.name = initialize_name()

    # reset the robot's name
    def reset(self):
        self.__init__()