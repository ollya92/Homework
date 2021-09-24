def get_digits(num: int) -> tuple[int]:
    """ Returns a tuple of digits """
    output = []
    while num > 0:
        digit = num % 10
        output.append(digit)
        num = num // 10
    output = reversed(output)
    return tuple(output)


if __name__ == '__main__':
    print(get_digits(87178291199))

