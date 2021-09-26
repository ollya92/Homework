"""
Implement a decorator `remember_result` which remembers last result of function
it decorates and prints it before next call.
"""


import functools

def remember_result(func):
        """Remembers last result of function"""
        before_value = [None]
        @functools.wraps(func)
        def wrapper(*args):
            print(f"Last result: {before_value[0]}")
            res = func(*args)
            before_value[0] = res
        return wrapper


@remember_result
def sum_list(*args):
    """Returns a sum of values"""
    result = ""
    if isinstance(args[0], int):
        result = 0
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result


if __name__ == "__main__":
    sum_list("a", "b")
    sum_list("abc", "cde")
    sum_list(3, 4, 5)

