"""
Implement your custom iterator class called MySquareIterator which gives squares of elements of collection
it iterates through.
"""


class MySquareIterator:
    def __init__(self, obj):
        if isinstance(obj, (list, tuple)):
            self._obj = obj
        else:
            raise TypeError(f"Need an iterable object!")
        for item in self._obj:
            if isinstance(item, (int, float)):
                self._index = 0
            else:
                raise TypeError(f"Need iterable object contains only digits!")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            square_item = self._obj[self._index] ** 2
            self._index += 1
            return square_item
        except IndexError:
            raise StopIteration


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    itr = MySquareIterator(lst)
    for value in itr:
        print(value, end=" ")

