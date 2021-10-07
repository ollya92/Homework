"""
Implement your custom collection called MyNumberCollection.
It should be able to contain only numbers.
It should NOT inherit any other collections.
If user tries to add a string or any non numerical object there, exception TypeError should be raised.
Method init should be able to take either start,end,step arguments, where start - first number of collection,
end - last number of collection or some ordered iterable collection (see the example).
Implement following functionality:
1)appending new element to the end of collection
2)concatenating collections together using +
3)when element is addressed by index(using []), user should get square of the addressed element.
4)when iterated using cycle for, elements should be given normally
5)user should be able to print whole collection as if it was list. Example:

"""


class MyNumberCollection:
    def __init__(self, start, end=None, step=None):
        self.my_collection = []
        self._index = 0
        if isinstance(start, (int, float)) and isinstance(end, (int, float)) and isinstance(step, (int, float)):
            self._start = start
            self._end = end
            self._step = step
            for num in range(self._start, self._end, self._step):
                self.my_collection.append(num)
            if self._end not in self.my_collection:
                self.my_collection.append(self._end)
        elif isinstance(start, (tuple, list, set)):
            for num in start:
                if isinstance(num, (int, float)):
                    self.my_collection.append(num)
                else:
                    raise TypeError(f"Only numerical type!")
        else:
            raise TypeError(f"Only numerical type!")

    def add_to_end(self, value):
        """Add value to the end of collection"""
        self._value = value
        if isinstance(self._value, (int, float)):
            self.my_collection.append(self._value)
        else:
            raise TypeError(f"'{self._value}'-object is not a number!")

    def __add__(self, value):
        """Concatenate two collections """
        if isinstance(value, MyNumberCollection):
            return self.my_collection + value.my_collection
        else:
            raise TypeError(f"Only numerical type!")

    def __getitem__(self, ind):
        """Square of value under entered index"""
        if ind <= len(self.my_collection):
            return self.my_collection[ind] ** 2
        else:
            raise IndexError(f"There is no element with such index!")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self._item = self.my_collection[self._index]

        except IndexError:
            raise StopIteration
        self._index += 1
        return self._item

    def __str__(self):
        return f"{self.my_collection}"


if __name__ == "__main__":
    col1 = MyNumberCollection(0, 5, 2)
    print(col1)

    col2 = MyNumberCollection((1, 2, 3, 4, 5))
    print(col2)

    col3 = MyNumberCollection((1, 2, 3, "4", 5))

    col1.add_to_end(7)
    print(col1)

    col2.add_to_end("string")

    print(col1 + col2)
    print(col1)
    print(col2)
    print(col2[12])
    for item in col1:
        print(item, end=" ")

