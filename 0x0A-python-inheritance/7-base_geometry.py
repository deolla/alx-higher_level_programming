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
        Raises:
            Exception: with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates values.

        Raises:
            TypeError: if not integer.
            ValueError: if not greater than 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
