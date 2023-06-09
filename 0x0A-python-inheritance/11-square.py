#!/usr/bin/python3
"""
A class Square that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square that inherits from Rectangle

    Attribute:
        size: size of square.
    """
    def __init__(self, size):
        """
        Initilize a square.

        Args:
            Size (int): The size of a square.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculate the area of a square.

        Returns:
            return the area of a square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns:
            return the square description: [Square] <width>/<height>
        """
        return f"[Square] {self.__size}/{self.__size}"
