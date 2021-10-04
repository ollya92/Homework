"""
Create hierarchy out of birds. Implement 4 classes:
1.class Bird with an attribute name and methods fly and walk.
2.class FlyingBird with attributes name, ration, and with the same methods.
ration must have default value. Implement the method eat which will describe its typical ration.
3.class NonFlyingBird with same characteristics but which obviously without attribute fly.
Add same "eat" method but with other implementation regarding the swimming bird tastes.
4.class SuperBird which can do all of it: walk, fly, swim and eat. But be careful which "eat" method you inherit.
Implement str() function call for each class.
Have a look at mro method of your last class.
"""


class Bird:
    def __init__(self, name):
        self._name = name

    def fly(self):
        print(f"{self._name} can fly!")

    def walk(self):
        print(f"{self._name} can walk!")

    def __str__(self):
        return f"{self._name} can fly and walk!"


class FlyingBird(Bird):
    def __init__(self, name, ration="grains"):
        self._ration = ration
        super().__init__(name)

    def eat(self):
        print(f"{self._name} eats mostly {self._ration}")

    def __str__(self):
        return f"{self._name} can fly and walk!"


class NonFlyingBird(Bird):
    def __init__(self, name, ration="fish"):
        self._ration = ration
        super().__init__(name)

    def swim(self):
        print(f"{self._name} can swim!")

    def eat(self):
        print(f"{self._name} eats mostly {self._ration}!")

    def __getattribute__(self, item):
        if item == "fly":
            raise AttributeError(f"{self._name} object has no attribute {item}")
        else:
            return object.__getattribute__(self, item)

    def __str__(self):
        return f"{self._name} can walk and swim!"


class SuperBird(FlyingBird, NonFlyingBird):
    def __init__(self, name):
        super().__init__(name)

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __str__(self):
        return f"{self._name} bird can fly, walk and swim!"


if __name__ == "__main__":
    b = Bird("Any")
    b.walk()

    p = NonFlyingBird("Penguin")
    p.swim()
    p.fly()
    p.eat()

    c = FlyingBird("Canary")
    print(str(c))
    c.eat()

    s = SuperBird("Gull")
    print(str(s))
    s.eat()

    print(SuperBird.__mro__)

