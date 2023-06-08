#!/usr/bin/python3
# Author = Osuji Anthony
"""print the numbesr from 1 to 100 separated by a space.
    for multiples of three, print fizz instead of the number
    for multiple of five, print Buzz instead of the number.
    for multiple of three and five. print FizzBuxx instead of the numbers.
    """

def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("Fizzbuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5  == 0:
            print("BUzz ", end="")
        else:
            print("{}".format(number), end="")
