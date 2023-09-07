verses_dict = {
    12: (None, "the horse and the hound and the horn"),
    11: ("that belonged to", "the farmer sowing his corn"),
    10: ("that kept", "the rooster that crowed in the morn"),
    9: ("that woke", "the priest all shaven and shorn"),
    8: ("that married", "the man all tattered and torn"),
    7: ("that kissed", "the maiden all forlorn"),
    6: ("that milked", "the cow with the crumpled horn"),
    5: ("that tossed", "the dog"),
    4: ("that worried", "the cat"),
    3: ("that killed", "the rat"),
    2: ("that ate", "the malt"),
    1: ("that lay in", "the house that Jack built."),
}

def get_verse(verse_number):
    result = f"This is"
    for i in range(verse_number, 0, -1):
        if i != 1:
            result += f" {verses_dict[i][1]} {verses_dict[i-1][0]}"
        else: # there is no action after the last verse
            result += f" {verses_dict[i][1]}"
    return result


def recite(start_verse, end_verse):
    verses = []
    for i in range(start_verse, end_verse+1):
        verses.append(get_verse(i))
    return verses