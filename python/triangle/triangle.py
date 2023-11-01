def is_triangle(sides):
    a, b, c = sides
    if a == 0 or b == 0 or c == 0:
        return False
    if not (a + b >= c):
        return False
    if not (b + c >= a):
        return False
    if not (a + c >= b):
        return False
    return True

def equilateral(sides):
    a, b, c = sides
    return a == b == c and a == c if is_triangle(sides) else False


def isosceles(sides):
    a, b, c = sides
    return a == b or b == c or a == c if is_triangle(sides) else False


def scalene(sides):
    a, b, c = sides
    return a != b != c and a != c if is_triangle(sides) else False
