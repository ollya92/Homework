"""
Implement function for check that number is even and is greater than 2.
Throw different exceptions for this errors.
Custom exceptions must be derived from custom base exception(not Base Exception class).
"""


class AllException(Exception):
    pass


class LessTwoError(AllException):
    pass


class NotEvenError(AllException):
    pass


class NotIntegerError(AllException):
    pass


def even_value(num):
    if not isinstance(num, int):
        raise NotIntegerError(f"Number should be integer type!")
    elif num <= 2:
        raise LessTwoError(f"Number should be more than 2!")
    elif num % 2 != 0:
        raise NotEvenError(f"Number should be even!")
    else:
        return f"Your number is even!"


if __name__ == "__main__":
    print(even_value(1.4))
    print(even_value("s"))
    print(even_value(0))
    print(even_value(3))
    print(even_value(8))

