def triplets_with_sum(number):
    return [[a, b, c] for a, b, c in create_triplet(number) if a * a + b * b == c * c]


def create_triplet(number):
    for a in range(number // 3 + 1):
        for b in range(a, (number - a + 1) // 2):
            c = number - a - b
            yield [a, b, c]
