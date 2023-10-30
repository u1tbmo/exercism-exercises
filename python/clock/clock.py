class Clock:
    def __init__(self, hour, minute):
        self.hour, self.minute = self.normalize(hour, minute)

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}"

    def __eq__(self, other):
        other_hour, other_minute = self.normalize(other.hour, other.minute)
        if self.hour == other_hour and self.minute == other_minute:
            return True
        else:
            return False

    def __add__(self, minutes):
        self.minute += minutes
        self.hour, self.minute = self.normalize(self.hour, self.minute)
        return self

    def __sub__(self, minutes):
        self.minute -= minutes
        self.hour, self.minute = self.normalize(self.hour, self.minute)
        return self

    def normalize(self, hour, minute):
        # Normalize input time
        while minute >= 60 or minute < 0:
            hour += 1 if minute >= 0 else -1
            minute -= 60 if minute >= 0 else -60

        while hour >= 24 or hour < 0:
            hour -= 24 if hour >= 24 else -24
        
        return (hour, minute)