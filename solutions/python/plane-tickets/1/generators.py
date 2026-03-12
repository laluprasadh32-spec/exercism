"""Functions to automate Conda airlines ticketing system."""

def generate_seat_letters(number):
    """Generate a series of letters for airline seats."""

    letters = ["A", "B", "C", "D"]

    for i in range(number):
        yield letters[i % 4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats."""

    row = 1
    count = 0

    while count < number:

        if row == 13:  # skip row 13
            row += 1
            continue

        for letter in ["A", "B", "C", "D"]:

            if count >= number:
                break

            yield str(row) + letter
            count += 1

        row += 1


def assign_seats(passengers):
    """Assign seats to passengers."""

    seats = generate_seats(len(passengers))
    result = {}

    for passenger in passengers:
        result[passenger] = next(seats)

    return result


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket."""

    for seat in seat_numbers:
        code = seat + flight_id
        code = code.ljust(12, "0")
        yield code