gifts_dict = {
    1: "a Partridge in a Pear Tree",
    2: "two Turtle Doves",
    3: "three French Hens",
    4: "four Calling Birds",
    5: "five Gold Rings",
    6: "six Geese-a-Laying",
    7: "seven Swans-a-Swimming",
    8: "eight Maids-a-Milking",
    9: "nine Ladies Dancing",
    10: "ten Lords-a-Leaping",
    11: "eleven Pipers Piping",
    12: "twelve Drummers Drumming"
}

day_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh','twelfth']

def get_gifts(current_verse):
    gift_list = []
    for i in range(current_verse, 0, -1): # range(x,y,z), y is excluded, the number before 0 with a step of -1 is 1
        gift_list.append(gifts_dict[i])
    if current_verse > 1:
        gift_list[-1] = "and " + gift_list[-1]
    return ', '.join(gift_list)

def recite(start_verse, end_verse): # start_verse is the number of gifts to start with, end_verse is the number of gifts to end with
    # initialize a list of verses
    verses = []

    for i in range(start_verse, end_verse + 1): # recite(1,1) => range(1,2) => 1
        # get the gifts for the current verse, and append
        verses.append(f"On the {day_list[i-1]} day of Christmas my true love gave to me: {get_gifts(i)}.")

    # print(verses)
    return verses

print(recite(5,6))