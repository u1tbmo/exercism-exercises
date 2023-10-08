def saddle_points(matrix):
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise ValueError("irregular matrix")

    potential_saddle_points = []
    col_list = list(zip(*matrix))

    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(col_list):
            if max(row) == min(col):
                potential_saddle_points.append({"row": row_index + 1, "column": col_index + 1})

    return potential_saddle_points
