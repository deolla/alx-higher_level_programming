#!/usr/bin/python3
"""
A function that returns True if the object is exactly class.
"""


def is_same_class(obj, a_class):
    """
    Returns:
         returns True if the object is exactly an instance of the specified
         class ; otherwise False.
    """
    return type(obj) is a_class
