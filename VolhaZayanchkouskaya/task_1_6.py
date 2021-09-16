"""
Write a Python program to convert a given tuple of positive integers into an integer.
Examples:
Input: (1, 2, 3, 4)
Output: 1234
"""
tuple_in = (1, 2, 3, 4)
tuple_out = int(''.join(map(str, tuple_in)))
print(tuple_out)
