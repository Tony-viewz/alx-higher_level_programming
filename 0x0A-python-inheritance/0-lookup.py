#!/usr/bin/python3
"""A function that returns the list of available attributes ."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
