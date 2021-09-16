"""
Write a Python program to calculate the length of a string without using the `len` function.
"""

input_string = input("Enter a string: ")
count_chr = 0
for character in input_string:
    count_chr += 1
print(count_chr)
