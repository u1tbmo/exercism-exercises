def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    count = 0
    for index, letter in enumerate(strand_a):
        if strand_a[index] != strand_b[index]:
            count += 1
    return count