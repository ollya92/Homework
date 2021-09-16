"""
Write a program which makes a pretty print of a part of the multiplication table.
Examples:
Input:
a = 2
b = 4
c = 3
d = 7
Output:
	3	4	5	6	7
2	6	8	10	12	14
3	9	12	15	18	21
4	12	16	20	24	28
"""

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))
print(end='\t')
for multiplier2 in range(c, d + 1):
    print(multiplier2, end='\t')
for multiplier1 in range(a, b + 1):
    print(end='\n')
    print(multiplier1, end='\t')
    for multiplier2 in range(c, d + 1):
        print(multiplier1 * multiplier2, end='\t')
