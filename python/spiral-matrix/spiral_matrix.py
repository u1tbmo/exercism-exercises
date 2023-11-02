def spiral_matrix(size: int) -> list[list[int]]:
    if size <= 0:
        return []

    matrix = [[0] * size for _ in range(size)]

    directions = ['E', 'S', 'W', 'N']

    # Restrictions
    left_r = 0
    right_r = size - 1
    top_r = 0
    bottom_r = size - 1

    num = 1
    direction_counter = 0
    while num <= size**2:
        direction = directions[direction_counter % 4]
        if direction == 'E':
            for i in range(left_r, right_r + 1):
                matrix[top_r][i] = num
                num += 1
            top_r += 1
        elif direction == 'S':
            for i in range(top_r, bottom_r + 1):
                matrix[i][right_r] = num
                num += 1
            right_r -= 1
        elif direction == 'W':
            for i in range(right_r, left_r - 1, -1):
                matrix[bottom_r][i] = num
                num += 1
            bottom_r -= 1
        elif direction == 'N':
            for i in range(bottom_r, top_r - 1, -1):
                matrix[i][left_r] = num
                num += 1
            left_r += 1
        direction_counter += 1

    return matrix