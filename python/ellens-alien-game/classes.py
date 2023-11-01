"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    health = 3
    total_aliens_created = 0

    def __init__(self, location_x, location_y):
        self.x_coordinate = location_x
        self.y_coordinate = location_y
        Alien.total_aliens_created += 1

    def hit(self):
        self.health -= 1

    def is_alive(self):
        return self.health >= 1

    def teleport(self, teleport_x, teleport_y):
        self.x_coordinate = teleport_x
        self.y_coordinate = teleport_y

    def collision_detection(self, other_object):
        pass

def new_aliens_collection(alien_start_positions):
    alien_list = []
    for location in alien_start_positions:
        location_x, location_y = location
        alien_list.append(Alien(location_x, location_y))
    return alien_list
    