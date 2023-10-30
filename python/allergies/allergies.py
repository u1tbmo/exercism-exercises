class Allergies:
    def __init__(self, score):
        self.possible_allergies = {
            1024: None,
            512: None,
            256: None,
            128: "cats",
            64: "pollen",
            32: "chocolate",
            16: "tomatoes",
            8: "strawberries",
            4: "shellfish",
            2: "peanuts",
            1: "eggs",
        }

        self.allegry_lst = {
            1024: False,
            512: False,
            256: False,
            128: False,
            64: False,
            32: False,
            16: False,
            8: False,
            4: False,
            2: False,
            1: False,
        }

        self.lst = []

        for k in self.possible_allergies.keys():
            if score >= k:
                self.allegry_lst[k] = True
                if self.possible_allergies[k] != None:
                    self.lst.append(self.possible_allergies[k])
                score -= k
            else:
                self.allegry_lst[k] = False

    def allergic_to(self, item):
        if item in self.lst:
            return True
        else:
            return False
    
print(Allergies(257).lst)