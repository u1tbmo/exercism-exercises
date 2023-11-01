# Modified from original solution by Sublow.
# https://stackoverflow.com/a/58730468
def factorize(number):
    return [n for n in range(1, number) if not number % n]

def classify(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    factors_list = factorize(number)
    aliquot_sum = sum(factors_list)
    
    return "perfect" if aliquot_sum == number else "abundant" if aliquot_sum > number else "deficient"
