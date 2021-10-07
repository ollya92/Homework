"""
Implement context manager for opening and working with file,
including handling exceptions with @contextmanager decorator.
"""


from contextlib import contextmanager


@contextmanager
def open_file(path, mode):
    try:
        file = open(path, mode)
        yield file
    except OSError:
        print("We had an error!")
    finally:
        file.close()


if __name__ == "__main__":
    with open_file('task7_2.txt', 'a') as f:
        f.write('Session 7 \n')

