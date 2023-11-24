def largest(min_factor: int, max_factor: int):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if not valid_range(min_factor, max_factor):
        raise ValueError("min must be <= max")

    factors: set[tuple[int, int]] = set()
    largest_palindrome: int | None = 0

    for x in range(max_factor, min_factor - 1, -1):
        was_bigger = False
        for y in range(max_factor, min_factor - 1, -1):
            product = x * y
            if product >= largest_palindrome:
                was_bigger = True
                if is_palindrome(product):
                    if product > largest_palindrome:
                        factors.clear()
                    largest_palindrome = product
                    factors.add((x, y))
        if not was_bigger:
            break
    if largest_palindrome == 0:
        largest_palindrome = None

    return largest_palindrome, factors


def smallest(min_factor: int, max_factor: int):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    if not valid_range(min_factor, max_factor):
        raise ValueError("min must be <= max")

    factors: set[tuple[int, int]] = set()
    smallest_palindrome: int | None = 0

    for x in range(min_factor, max_factor + 1):
        was_smaller = False
        for y in range(min_factor, max_factor + 1):
            product = x * y
            if product <= smallest_palindrome or smallest_palindrome == 0:
                was_smaller = True
                if is_palindrome(product):
                    if product < smallest_palindrome:
                        factors.clear()
                    smallest_palindrome = product
                    factors.add((x, y))
        if not was_smaller:
            break
    if smallest_palindrome == 0:
        smallest_palindrome = None

    return smallest_palindrome, factors


def valid_range(min_factor: int, max_factor: int) -> bool:
    """Check if the range is valid.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: bool True if the range is valid
    """
    return min_factor <= max_factor


def is_palindrome(number: int) -> bool:
    """Check if a number is a palindrome

    :param number: int
    :return: bool
    """

    return str(number) == str(number)[::-1]
