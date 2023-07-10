#!/usr/bin/python3

"""
A class BaseGeometry (based on 5-base_geometry.py).
"""


class BaseGeometry:
    """
    A class BaseGeometry.
    """

    def area(self):
        """
        Method not implemented.

        Raises:
            Exception: with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates  a values as an integer

        Raises:
            TypeError: if not integer.
            ValueError: if not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
