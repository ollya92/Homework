"""
A singleton is a class that allows only a single instance of itself to be created
and gives access to that created instance. Implement singleton logic inside your custom class
using a method to initialize class instance.

Example:

p = Sun.inst()
f = Sun.inst()
p is f
True
"""


class Sun():

    obj = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.obj, cls):
            cls.obj = object.__new__(cls, *args, **kwargs)
        return cls.obj

    @staticmethod
    def inst():
        return Sun()


if __name__ == "__main__":
    p = Sun.inst()
    f = Sun.inst()
    print(p is f)