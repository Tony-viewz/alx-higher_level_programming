#!/usr/bin/python3

if __name__ == "__main__":
    """ prints the result of the addition 1 + 2 = 3."""
    a = 1
    b = 2
    from add_0 import add
    result = add(a, b)

    print("{} + {} = {}".format(a, b, result))
