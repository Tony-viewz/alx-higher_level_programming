#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """A function that finds all multiples of 2 in a list."""
    outcome = []
    for num in range(len(my_list)):
        if my_list[num] % 2 == 0:
            outcome.append(True)
        else:
            outcome.append(False)

    return (outcome)
