#!/usr/bin/python3

"""
This is a class Square that defines a square.
"""


class Square:
    """
    This class represents a sqaure.

    Attributes:
        __size (int): The size of sqaure.
    """

    def __init__(self, size=0):
        """
        Initialises a square instance with an optional size.

        Args:
            size (int): The size of the sqaure. Default to 0.

        Raises:
            TypeError: If size is not an integer,
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
