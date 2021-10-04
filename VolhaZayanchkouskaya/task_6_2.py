"""
Implement custom dictionary that will memorize 10 latest changed keys.
Using method "get_history" return this keys.

Example:

d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
d.get_history()

["bar"]
After your own implementation of the class have a look at collections.deque
https://docs.python.org/3/library/collections.html#collections.deque
"""


class HistoryDict:
    total_keys = 10

    def __init__(self, dictionary={}):
        self._history = []
        self._dict = dictionary

    def set_value(self, key: str, value: int):
        self._dict[key] = value
        if len(self._history) < HistoryDict.total_keys:
            self._history.append(key)
        else:
            self._history.pop(0)
            self._history.append(key)

    def get_history(self):
        print(self._history)


if __name__ == "__main__":
    d = HistoryDict({"foo": 42})
    d.set_value("bar", 43)
    d.get_history()

