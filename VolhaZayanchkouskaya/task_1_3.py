"""
Write a Python program that accepts a comma separated sequence of words
as input and prints the unique words in sorted form.
Examples:
Input: ['red', 'white', 'black', 'red', 'green', 'black']
Output: ['black', 'green', 'red', 'white', 'red']
"""

input_str = ['red', 'white', 'black', 'red', 'green', 'black']
output_str = []
for item in input_str:
    if item not in output_str:
        output_str.append(item)
print(sorted(output_str))
