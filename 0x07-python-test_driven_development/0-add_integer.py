#!/usr/bin/python3

"""
This is a function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    Function that two integer or float numbers.

    Args:
        a: integers or floats.
        b: integers or floats.

    Raises:
        TypeError: if a or b are integers or floats.

    Returns:
        The sum of two arguments.
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
