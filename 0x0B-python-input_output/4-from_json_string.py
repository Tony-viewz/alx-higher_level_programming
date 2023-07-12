#!/usr/bin/python3
# 6-from_json_string.py
"""A function that returns an object (Python data structure)."""
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string."""
    return json.loads(my_str)
