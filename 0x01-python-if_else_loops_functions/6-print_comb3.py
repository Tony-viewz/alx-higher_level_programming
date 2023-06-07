#!/usr/bin/python3
# Author - Osuji Anthony
for digits in range(0, 10):
    for digit0 in range(digits +1, 10):
        if digits == 8 and digit0 == 9:
            print("{}{}".format(digits, digit0))
        else:
            print("{}{}".format(digits, digit0), end=", ")
