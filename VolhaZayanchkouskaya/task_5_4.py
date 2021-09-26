"""
Look through file `modules/legb.py`.

1) Find a way to call `inner_function` without moving it from inside of `enclosed_function`.

2.1) Modify ONE LINE in `inner_function` to make it print variable 'a' from global scope.

2.2) Modify ONE LINE in `inner_function` to make it print variable 'a' from enclosing function.

"""


a = "I am global variable!"


def enclosing_funcion():
    """"""
    a = "I am variable from enclosed function!"

    def inner_function():
        a = "I am local variable!"
        print(a)

    inner_function()


def enclosing_funcion21():
    a = "I am variable from enclosed function!"

    def inner_function21():
        global a
        print(a)

    inner_function21()


def enclosing_funcion22():
    a = "I am variable from enclosed function!"

    def inner_function22():
        nonlocal a
        print(a)

    inner_function22()


if __name__ == "__main__":
    enclosing_funcion()
    enclosing_funcion21()
    enclosing_funcion22()

