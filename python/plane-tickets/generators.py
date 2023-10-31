"""Functions to automate Conda airlines ticketing system."""

seat_letters = "ABCD"

def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    for i in range(number):
        yield seat_letters[i % 4]
    


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    for i in range(number):
        if i // 4 + 1 >= 13:
            yield f"{i // 4 + 2}{seat_letters[i % 4]}"
        else:
            yield f"{i // 4 + 1}{seat_letters[i % 4]}"
            

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    
    seat_assignment = {}
    seats = generate_seats(len(passengers))
    for p in passengers:
        seat_assignment[p] = next(seats)
    return seat_assignment

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat_number in seat_numbers:
        yield f"{seat_number + flight_id:<012}"