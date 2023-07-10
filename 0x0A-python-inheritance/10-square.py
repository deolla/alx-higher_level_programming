#!/usr/bin/python3

"""
A class Square that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle

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
        super().__init__(size, size)
        self.__size = size
