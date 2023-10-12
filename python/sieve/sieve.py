def primes(limit):
    # create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n)
    numbers = list(range(2, limit + 1))

    # initially, let p equal 2, the smallest prime number
    p = 2

    running = True
    while running:
        # remove the multiples of p by counting in increments of p from 2p to n
        for i in range(2 * p, limit + 1, p):
            # mark the multiples of p in the list
            if i in numbers:
                numbers.remove(i)

        # find the smallest number in the list greater than p that is not marked
        for x in sorted(numbers):
            if x > p:
                p = x
                break
        # if there was no such number, stop
        else:
            running = False

    return numbers
