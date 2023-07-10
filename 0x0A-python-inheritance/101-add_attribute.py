#!/usr/bin/python3
"""
A function that adds a new attribute to an object.
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if possible
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("Can't add new attribute")
    else:
        setattr(obj, attr, value)
