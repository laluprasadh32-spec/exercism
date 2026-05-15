def is_valid(isbn):
    # Remove hyphens
    isbn = isbn.replace("-", "")
    
    # ISBN must be 10 characters
    if len(isbn) != 10:
        return False

    total = 0

    for i in range(10):
        char = isbn[i]

        # Last character can be X
        if char == 'X':
            if i != 9:
                return False
            value = 10
        elif char.isdigit():
            value = int(char)
        else:
            return False

        total += value * (10 - i)

    return total % 11 == 0