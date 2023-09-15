class Luhn:
    def __init__(self, card_num):
        while " " in card_num:
            card_num = card_num.replace(" ", "")
        self.card_num = card_num

    def valid(self):
        card_num = self.card_num

        # Error checking
        if len(card_num) <= 1:
            return False
        for i in card_num:
            if i.isnumeric() is False:
                return False
        
        # Turn the card number into a list of integers
        card_num = [int(i) for i in card_num]
        # Create a list of every other number starting from the right
        nums_to_double = card_num[-2::-2] # [-2::-2] starts at the second index from the right and goes to the left by 2

        # Double every other number starting from the right
        for index, number in enumerate(nums_to_double):
            nums_to_double[index] = number * 2

        # Check for double digit numbers and subtract 9 if the number is greater than 9
        for index, number in enumerate(nums_to_double):
            if len(str(number)) == 2:
                nums_to_double[index] = number - 9 # subtracts 9 from the number if it is greater than 9

        # Assigns the list of numbers to double to the card number
        card_num[-2::-2] = nums_to_double

        if sum(card_num) % 10 == 0:
            return True
        else:
            return False