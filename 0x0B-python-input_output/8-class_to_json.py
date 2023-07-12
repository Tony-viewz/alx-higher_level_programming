#!/usr/bin/python3
"""A function that returns the description with data structure."""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
