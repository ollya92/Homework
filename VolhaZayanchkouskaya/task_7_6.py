"""
Create console program for proving Goldbach's conjecture.
Program accepts number for input and print result. For pressing 'q' program succesfully close.
Use function from Task 5.5 for validating input, handle all exceptions and print user friendly output.
"""

from task_7_5 import *


def is_prime(n):
    """Check number is prime or not"""
    flag = 0
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            flag = 1
    if flag == 1:
        return False
    else:
        return True


def goldbach():
    """Check that whole even number is a sum of two prime numbers"""
    number = input("Enter an even integer number greater than 2 or 'q' to exit: ")
    if number.lower() == "q":
        return f"Exit!"
    else:
        number = int(number)
        if number % 2 != 0:
            raise NotEvenError(f"Number should be even!")
        elif number <= 2:
            raise LessTwoError(f"Number should be greater than 2!")
        else:
            for first_num in range(1, number):
                second_num = number - first_num
                if is_prime(first_num) and is_prime(second_num):
                    return f"Goldbach was right: {number} = {first_num} + {second_num}"


if __name__ == "__main__":
    print(goldbach())

