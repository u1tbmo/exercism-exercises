class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.planet_factors = {
            'mercury': 7600521.6,
            'venus': 19414080,
            'earth': 31556952,
            'mars': 59356800,
            'jupiter': 374222560,
            'saturn': 929596608,
            'uranus': 2651486400,
            'neptune': 5200418592
        }

    def on_planet(self, planet):
        return round(self.seconds / self.planet_factors[planet], 2)
