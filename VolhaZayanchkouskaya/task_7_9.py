"""
Implement an iterator class EvenRange, which accepts start and end of the interval as an init arguments
and gives only even numbers during iteration.
If user tries to iterate after it gave all possible numbers Out of numbers! should be printed.
Note: Do not use function range() at all.
"""


class EvenRange:
    def __init__(self, start, end):
        if isinstance(start, int) and isinstance(end, int):
            self._start = start
            self._end = end
            self._index = 0
        else:
            raise TypeError(f"Both of numbers should be integer!")
        self.even_list = []
        while self._start <= self._end:
            if self._start % 2 == 0:
                self.even_list.append(self._start)
                self._start += 1
            else:
                self._start += 1

    def __iter__(self):
        return self

    def __next__(self):
        try:
            even_value = self.even_list[self._index]
        except IndexError:
            print(f"Out of numbers!")
            raise StopIteration
        self._index += 1
        return even_value


if __name__ == "__main__":
    er1 = EvenRange(7, 11)
    print(next(er1))
    print(next(er1))

    er2 = EvenRange(3, 14)
    for number in er2:
        print(number, end=" ")





