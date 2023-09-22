# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    # initialize result
    result = 0
    # sort the dice
    dice.sort()

    # if category is a countable category
    match category:
        case 1:
            result = dice.count(1) * 1
        case 2:
            result = dice.count(2) * 2
        case 3:
            result = dice.count(3) * 3
        case 4:
            result = dice.count(4) * 4
        case 5:
            result = dice.count(5) * 5
        case 6:
            result = dice.count(6) * 6
    
    # if category is a non-countable category
    match category:
        case 0: # YACHT - all dice are the same
            result = 50 if len(set(dice)) == 1 else 0
        case 7: # FULL_HOUSE - three of one number and two of another
            if dice.count(max(dice, key=dice.count)) == 3 and dice.count(min(dice, key=dice.count)) == 2:
                result = sum(dice)
        case 8: # FOUR_OF_A_KIND - at least four dice showing the same face
            if dice.count(max(dice, key=dice.count)) >= 4:
                result = 4 * max(dice, key=dice.count)
        case 9: # LITTLE_STRAIGHT - 1-2-3-4-5
            if dice == [1, 2, 3, 4, 5]:
                result = 30
        case 10: # BIG_STRAIGHT - 2-3-4-5-6
            if dice == [2, 3, 4, 5, 6]:
                result = 30
        case 11: # CHOICE - sum of the dice
            result = sum(dice)

    return result