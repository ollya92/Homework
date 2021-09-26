"""
Implement a decorator `call_once` which runs a function or method once and caches the result.
All consecutive calls to this function should return cached result no matter the arguments.

```python
@call_once
def sum_of_numbers(a, b):
    return a + b

"""


import functools


def call_once(func):
    """Returns a cache value of function"""
    def wrapper(*args, **kwargs):
        if not wrapper.cashed:
            wrapper.value = func(*args, **kwargs)
            wrapper.cashed = True
        return wrapper.value
    wrapper.cashed = False
    return functools.update_wrapper(wrapper, func)

@call_once
def sum_of_numbers(a, b):
    """Returns a sum of two numbers"""
    return a + b


if __name__ == "__main__":
    print(sum_of_numbers(13, 42))
    print(sum_of_numbers(999, 100))
    print(sum_of_numbers(134, 412))
    print(sum_of_numbers(856, 232))

