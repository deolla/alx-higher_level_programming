#!/usr/bin/python3
"""
A function that adds a new attribute to an object.
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if possible
    """
    if (
        hasattr(obj, '__dict__')
        or (hasattr(type(obj), '__slots__') and attr in type(obj).__slots__)
    ):
        setattr(obj, attr, value)
    else:
        raise TypeError("Can't add new attribute to the object")
