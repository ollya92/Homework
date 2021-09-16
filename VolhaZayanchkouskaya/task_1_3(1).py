"""
Create a program that asks the user for a number and then prints out a list of all
the [divisors](https://en.wikipedia.org/wiki/Divisor) of that number.
Examples:
Input: 60
Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}
"""
num = int(input("Enter a number: "))
divisors_set = set()
for div in range(1, num+1):
    if num % div == 0:
        divisors_set.add(div)
print(divisors_set)
