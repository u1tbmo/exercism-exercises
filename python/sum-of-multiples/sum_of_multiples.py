def sum_of_multiples(limit, multiples):
    resulting_set = set()
    for multiple in multiples:
        if multiple == 0:
            resulting_set.add(0)
            break
        for i in range(multiple, limit, multiple):
            resulting_set.add(i)
    return sum(resulting_set)