def largest_product(series: str, size: int):
    if size > len(str(series)):
        raise ValueError("span must be smaller than string length")
    if size < 0:
        raise ValueError("span must not be negative")
    if not series.isdigit():
        raise ValueError("digits input must only contain digits")

    slices: list[str] = []
    for i in range(len(str(series)) - size + 1):
        slices.append(series[i : i + size])

    max: int | None = None
    for slice in slices:
        slice_product = 1
        for digit in slice:
            slice_product *= int(digit)
        if max == None or slice_product > max:
            max = slice_product
    return max
