def combinations(target: int, size: int, exclude: list[int]) -> list[list[int]]:
    nums: list[int] = sorted([n for n in range(1, 10)], reverse=True)
    combination_list = []
    if size != 1:
        exclude += [n for n in nums if n - target >= 0]
    else:
        exclude += [n for n in nums if n != target]

    iter = 0
    while exclude != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        result, nums_to_exclude = find_combs(target, size, exclude.copy())
        if result:
            combination_list.append(result)
        exclude += [num for num in nums_to_exclude]
        exclude = sorted(list(set(exclude)))
        iter += 1

    return combination_list


def find_combs(target: int, size: int, exclude: list[int]) -> tuple[list, list]:
    nums: list[int] = sorted(
        [n for n in range(1, 10) if n not in exclude], reverse=True
    )

    result = []

    for num in nums:
        if target - num > 0 and size - 1 > 0:
            target -= num
            exclude += [num]
            result += [num]
            size -= 1
        elif target - num == 0 and size - 1 == 0:
            target -= num
            exclude += [num]
            result += [num]
            size -= 1
            return sorted(result), exclude
    return [], [result[0]]
