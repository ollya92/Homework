"""
Implement decorator with context manager support for writing execution time to log-file.
See contextlib module.
"""

from contextlib import ContextDecorator
from time import time, sleep
import math


class execution(ContextDecorator):

    def __enter__(self):
        self.t_start = time()
        sleep(0.5)
        return self

    def __exit__(self, *exc):
        self.t_end = time()
        with open("log_file.txt", "a") as logfile:
            logfile.writelines(f"Execution time {self.t_end - self.t_start: .2f} sec \n")
        return False


@execution()
def degree_func(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a ** b + math.sqrt(a + b)
    else:
        raise TypeError(f"Numbers should be integer!")


if __name__ == "__main__":
    print(degree_func(123, 67))

