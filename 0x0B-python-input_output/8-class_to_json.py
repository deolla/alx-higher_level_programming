#!/usr/bin/python3
"""
A function that returns the dictionary description with simple data structure.
"""


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure.

    Args:
        obj: object.
    """
    pop = {}
    if hasattr(obj, "__dict__"):
        pop = obj.__dict__.copy()
    return pop
