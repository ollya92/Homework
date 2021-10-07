"""
Implement decorator for supressing exceptions. If exception not occure write log to console.
"""

from contextlib import suppress
import logging

logging.basicConfig(level=logging.INFO)


def error_suppress(function):
    def wrapper(*args, **kwargs):
        with suppress(Exception):
            output = function(*args, **kwargs)
            logging.info("No exceptions!")
            return output
    return wrapper


@error_suppress
def some_func(a: int, b: int):
    return a / b


if __name__ == "__main__":
    print(some_func(3, 2.1))

