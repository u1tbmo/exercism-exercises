# Globals for the directions
# Change the values as you see fit
WEST = 0
NORTH = 1
EAST = 2
SOUTH = 3


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)
        self.actions = {
            "L": self.turn_left,
            "R": self.turn_right,
            "A": self.advance
        }

    def turn_left(self):
        self.direction = (self.direction - 1) % 4

    def turn_right(self):
        self.direction = (self.direction + 1) % 4

    def advance(self):
        moves = {
            NORTH: 1,
            SOUTH: -1,
            EAST: 1,
            WEST: -1
        }

        if self.direction in [NORTH, SOUTH]:
            self.coordinates = (self.coordinates[0], self.coordinates[1] + moves[self.direction])
        if self.direction in [EAST, WEST]:
            self.coordinates = (self.coordinates[0] + moves[self.direction], self.coordinates[1])

    def move(self, actions):
        for action in actions:
            self.actions[action]()
