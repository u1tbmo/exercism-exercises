class CustomSet:
    def __init__(self, elements: list = []):
        self.set = set()

        for e in elements:
            self.add(e)

    def isempty(self):
        return len(self.set) == 0

    def __contains__(self, element):
        return element in self.set

    def issubset(self, other):
        for e in self.set:
            if e not in other.set:
                return False
        return True

    def isdisjoint(self, other):
        for e in self.set:
            if e in other.set:
                return False
        return True

    def __eq__(self, other):
        return self.set == other.set

    def add(self, element):
        self.set.add(element)

    def intersection(self, other):
        return CustomSet([e for e in self.set if e in other.set])

    def __sub__(self, other):
        return CustomSet([e for e in self.set if e not in other.set])

    def __add__(self, other):
        return CustomSet(list(self.set) + list(other.set))
