#!/usr/bin/python3

"""
A function that prints a square with the character #.
"""

def print_square(size):
    """
    Print a square of '#' characters.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) is float:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
