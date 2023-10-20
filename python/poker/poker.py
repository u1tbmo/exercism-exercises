from collections import Counter

letter_vals = {
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}

def best_hands(hands):
    ranks = [determine_rank(hand) for hand in hands]
    max_rank = max(ranks)
    
    winning_hands = []
    for i, hand in enumerate(hands):
        if ranks[i] == max_rank:
            winning_hands.append(hand)

    return winning_hands

def common_values(hand):
    values = [card[:-1] for card in hand.split(' ')]

    nums = []
    for num in values:
        if num in letter_vals:
            nums.append(letter_vals[num])
        else:
            nums.append(int(num))
    
    nums.sort(reverse=True)

    return Counter(nums).most_common(5)

def determine_rank(hand):
    values, counts = zip(*common_values(hand))

    if values == (14, 5, 4, 3, 2):
        values = (5, 4, 3, 2, 1)

    # the hand is a flush if all of the suits are the same
    flush = len(set([card[-1] for card in hand.split(' ')])) == 1

    # the hand is a straight if the values are different and the difference between the min and max is 4
    straight = len(counts) == 5 and min(values) + 4 == max(values)

    ranking = 0

    # Straight Flush: the hand is both a straight and a flush
    if straight and flush:
        ranking = 8
    # Four of a Kind: four of the five cards in the hand have the same value
    elif counts[0] == 4:
        ranking = 7
    # Full House: three cards of the same value, with the remaining two cards forming a pair
    elif counts == (3,2):
        ranking = 6
    # Flush: the hand contains five cards of the same suit
    elif flush:
        ranking = 5
    # Straight: the hand contains five cards of sequential value
    elif straight:
        ranking = 4
    # Three of a Kind: three of the cards in the hand have the same value
    elif counts[0] == 3:
        ranking = 3
    # Two Pairs: two different pairs
    elif counts[:2] == (2,2):
        ranking = 2
    # One Pair: two of the five cards in the hand have the same value
    elif counts[0] == 2:
        ranking = 1
    # High Card: none of the above conditions are met

    return ranking, *values