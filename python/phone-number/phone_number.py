import string

allowed_punctuations = ["-", "(", ")", ".", "+"]
set_of_punctuations = set(string.punctuation)

for p in allowed_punctuations:
    set_of_punctuations.remove(p)

class PhoneNumber:
    number = ""
    area_code = ""

    # constructs a phone number object with the number and area code based on the phone number
    def __init__(self, phone_number):
        self.number = self.transform_number(phone_number)
        self.area_code = self.number[:3]

    # returns the number in the format (XXX)-XXX-XXXX
    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"

    # transforms the phone number into a clean number
    def transform_number(self, phone_number):
        clean_number = ""

        # appends only numbers to clean_number
        for c in phone_number:
            if c.isnumeric():
                clean_number += c
            # if c is not an allowed punctuation, raise error
            elif c in set_of_punctuations:
                raise ValueError("punctuations not permitted")
            # if there are letters, raise error, also makes sure that c is also not punctuation because .isalpha() returns true for punctuation
            elif (c.isalpha()) and (c not in string.punctuation):
                raise ValueError("letters not permitted")

        # check if number is not the expected length
        if len(clean_number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        elif len(clean_number) > 11:
            raise ValueError("must not be greater than 11 digits")
        
        # check if number is 11 digits
        if len(clean_number) == 11:
            # if the area code is not 1, raise error
            if clean_number[0] != "1":
                raise ValueError("11 digits must start with 1")
            # else, remove the 1
            else:
                clean_number = clean_number[1:]

        # check the exchange code
        if clean_number[3] == "0":
            raise ValueError("exchange code cannot start with zero")
        elif clean_number[3] == "1":
            raise ValueError("exchange code cannot start with one")
        
        # check the area code
        if clean_number[0] == "0":
            raise ValueError("area code cannot start with zero")
        elif clean_number[0] == "1":
            raise ValueError("area code cannot start with one")
        
        return clean_number