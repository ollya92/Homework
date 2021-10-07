"""
Implement a generator which will generate Fibonacci numbers endlessly.
"""


def endless_fib_generator():
    a1 = 1
    a2 = 1
    while True:
        yield a1
        a1, a2 = a2, a1 + a2


if __name__ == "__main__":
    gen = endless_fib_generator()
    while True:
        print(next(gen), end=" ")
