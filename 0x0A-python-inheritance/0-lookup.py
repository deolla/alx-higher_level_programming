#!/usr/bin/python3

"""
Write a function that returns the list of available attributes.
"""


def lookup(obj):
    """
    Returns:
        returns the list of available attributes and methods of an object:
    """
    att_list = []

    for m in dir(obj):
        att_list.append(m)
    return att_list
