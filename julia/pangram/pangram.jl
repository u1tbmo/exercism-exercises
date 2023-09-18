"""
    ispangram(input)

Return `true` if `input` contains every alphabetic character (case insensitive).

"""

function ispangram(input::AbstractString)
    # if the alphabet is a subset of the input, then it's a pangram
    return 'a':'z' ⊆ lowercase(input)
end
