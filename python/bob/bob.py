def response(hey_bob):
    phrase = hey_bob.strip()
    if phrase.endswith("?") and not phrase.isupper():
        return "Sure."
    elif phrase.endswith("?") and phrase.isupper():
        return "Calm down, I know what I'm doing!"
    elif phrase.isupper():
        return "Whoa, chill out!"
    elif not phrase:
        return "Fine. Be that way!"
    else:
        return "Whatever."
