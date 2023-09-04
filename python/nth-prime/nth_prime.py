def prime(number):
    if number < 1:
        raise ValueError("there is no zeroth prime")
    count = 0
    candidate = 2

    while True:
        if is_prime(candidate):
            count += 1
            if count == number:
                return candidate
        candidate += 1

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True