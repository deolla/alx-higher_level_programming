#!/usr/bin/pythoon3

"""
Define a MagicClass that represents a circle.
"""
import math


class MagicClass:
    """
    Define a MagicClass that represents a circle.

    Attributes:
        __radius (float or int): The radius of the circle.
    """
    def __init__(self, radius=0):
        """
        Initialise a Magiclass instance with the given radius.

        Args:
            radius (float or int): The radius of the circle. Defaults to 0.

        Raises:
            TypeError: If radius is not a number (float or integer).
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
