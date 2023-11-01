def annotate(minefield: list):
    if not minefield:
        return []
    
    # Check if minefield has no columns
    if not minefield[0]:
        return minefield
    
    # Check if minefield is rectangular
    valid_minefield = all([len(row) == len(minefield[0]) for row in minefield])
    if not valid_minefield:
        raise ValueError('The board is invalid with current input.')
    
    # Check for invalid characters
    for row in minefield:
        for char in row:
            if char not in ' *':
                raise ValueError('The board is invalid with current input.')

    minefield = [[j for j in i] for i in minefield]

    for i, row in enumerate(minefield):
        for j, cell in enumerate(row):
            if cell == ' ':
                neighbors = [
                    (i - 1, j - 1), # Up left
                    (i - 1, j), # Up
                    (i - 1, j + 1), # Up right
                    (i, j - 1), # Left
                    (i, j + 1), # Right
                    (i + 1, j - 1), # Down left
                    (i + 1, j), # Down
                    (i + 1, j + 1), # Down right
                ]

                count = 0
                for r, c in neighbors:
                    if 0 <= r < len(minefield) and 0 <= c < len(row) and minefield[r][c] == '*':
                        count += 1
                
                minefield[i][j] = str(count) if count > 0 else ' '

            else:
                minefield[i][j] = cell

    new_minefield = ["".join(lst) for lst in minefield]

    return new_minefield
