"""
Implement class-based context manager for opening and working with file, including handling exceptions.
Do not use 'with open()'. Pass filename and mode via constructor.
"""


class File:
    def __init__(self, file_name, mode):
        self._file_name = file_name
        self._mode = mode

    def __enter__(self):
        try:
            self._file = open(self._file_name, self._mode)
        except FileNotFoundError as ffe:
            raise ffe
        else:
            return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()


if __name__ == "__main__":
    with File("result7_1.txt", 'w') as opened_file:
        opened_file.write("Session 7")

