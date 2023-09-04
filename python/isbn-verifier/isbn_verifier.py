def is_valid(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    if not isbn[:-1].isdigit():
        return False
    if not (isbn[-1].isdigit() or isbn[-1] == 'X'):
        return False
    isbn = [int(num) if num.isdigit() else 10 for num in isbn]
    return sum([num * (10 - index) for index, num in enumerate(isbn)]) % 11 == 0