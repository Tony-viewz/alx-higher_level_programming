#!/usr/bin/python3
# 0-print_list_integer.py

def print_list_integer(my_list=[]):
    """A function that Prints all integers of a list."""
    for a in range(len(my_list)):
        print("{:d}".format(my_list[a]))

