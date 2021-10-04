"""
Implement a Counter class which optionally accepts the start value
and the counter stop value. If the start value is not specified
the counter should begin with 0.
If the stop value is not specified it should be counting up infinitely.
If the counter reaches the stop value, print "Maximal value is reached."

Implement to methods: "increment" and "get"

If you are familiar with Exception rising use it to display the
"Maximal value is reached." message.

"""


class Counter:
    def __init__(self, start=0, stop=None):
        self._start = start
        self._end = stop

    def increment(self):
        if self._end is not None and self._start >= self._end:
            print(f"Maximal value is reached")
        else:
            self._start += 1

    def get(self):
        return self._start


if __name__ == "__main__":
    c = Counter(stop=2)
    c.increment()
    print(c.get())
    c.increment()
    print(c.get())
    c.increment()
    print(c.get())
    
