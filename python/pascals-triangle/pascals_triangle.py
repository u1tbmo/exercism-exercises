def rows(row_count: int) -> list[list[int]]:
    triangle = []

    if row_count < 0:
        raise ValueError("number of rows is negative")

    if row_count == 0:
        return triangle
    if row_count == 1:
        triangle.append([1])
        return triangle

    triangle = rows(row_count - 1)

    prev_row = triangle[-1]

    current_row = [1]
    for i in range(len(prev_row) - 1):
        current_row.append(prev_row[i] + prev_row[i + 1])
    current_row.append(1)

    triangle.append(current_row)
    return triangle
