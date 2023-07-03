#!/usr/bin/python3

"""
This is a class Rectangle that defines a rectangle.
"""


class Rectangle:
    """
    This class defines a rectangle.

    Attributes:
        __width (int): The width of a rectangle.
        __height (int): The height of a rectangles.
    """
    def __init__(self, width=0, height=0):
        """
         Initialise a rectangle instance with the given width and height.

         Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Retrieve the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width of value to set.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
         Retrieve the height of the rectangle.

         Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            Value (int): The height of value to set.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
