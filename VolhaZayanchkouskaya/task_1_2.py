"""
Write a Python program to count the number of characters (character frequency) in
a string (ignore case of letters).
Examples:
Input: 'Oh, it is python'
Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}
"""

input_string = "Oh, it is python"
output_dict = {}
for character in input_string.lower():
    keys_dict = output_dict.keys()
    if character in keys_dict:
        output_dict[character] += 1
    else:
        output_dict[character] = 1
print(output_dict)
