def triplets_with_sum(number):
    list_of_triplets = []

    # a must be less than 1/3 of the number
    for a in range(1, number // 3):
        # b must be less than 1/2 of the number but greater than a
        for b in range(a + 1, number // 2):
            # since a + b + c = number, c = number - a - b using algebra
            c = number - a - b
            if a**2 + b**2 == c**2:
                list_of_triplets.append([a, b, c])
    return list_of_triplets
