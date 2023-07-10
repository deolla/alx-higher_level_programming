#!/usr/bin/python3
"""
A function that adds a new attribute to an object.
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if possible
    """
    if '__dict__' not in dir(obj):
        raise TypeError("Can't add new attribute")
    if '__slots__' in dir(obj):
        raise TypeError("Can't add new attribute")
    else:
        setattr(obj, attr, value)
