#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    """A function that removes all characters c and C from a string."""
    NewString = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(NewString))
