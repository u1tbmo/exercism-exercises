class CustomSet:
    def __init__(self, elements: list = []):
        self.elements = set()

        for e in elements:
            self.add(e)

    def isempty(self):
        return len(self.elements) == 0

    def __contains__(self, element):
        return element in self.elements

    def issubset(self, other):
        for e in self.elements:
            if e not in other.elements:
                return False
        return True

    def isdisjoint(self, other):
        for e in self.elements:
            if e in other.elements:
                return False
        return True

    def __eq__(self, other):
        return self.elements == other.elements

    def add(self, element):
        self.elements.add(element)

    def intersection(self, other):
        return CustomSet([e for e in self.elements if e in other.elements])

    def __sub__(self, other):
        return CustomSet([e for e in self.elements if e not in other.elements])

    def __add__(self, other):
        return CustomSet(list(self.elements) + list(other.elements))
