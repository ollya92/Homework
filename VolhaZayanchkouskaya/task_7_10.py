"""
Implement a generator which will generate odd numbers endlessly.
"""


def endless_generator():
    item = 1
    while True:
        yield item
        item += 2


if __name__ == "__main__":
    gen = endless_generator()
    while True:
        print(next(gen))
