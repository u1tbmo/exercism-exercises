# spell-checker: disable

import random, math

class Character:

    char_abilities = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']

    def __init__(self):
        for char_ability in self.char_abilities:
            setattr(self, char_ability, self.ability()) # set each ability

        # set hitpoints
        self.hitpoints = 10 + modifier(self.constitution) # type: ignore

    def ability(self):
        dice = [random.randint(1, 6) for i in range(4)] # rolls 4 dice
        dice.remove(min(dice)) # remove the smallest number
        return sum(dice) # return the sum of the remaining dice
        
def modifier(constitution):
    return math.floor((constitution - 10) / 2)