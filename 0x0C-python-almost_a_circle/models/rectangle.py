#!/usr/bin/python3

"""
This is a class Rectangle that inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """
    A class Rectangle that inherits from Base.

    Attributes:
        __width: width of the retangle.
        __height: height of the rectangle.
        __x: private attributes.
        __y: private attributes.

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialises a rectangle instance.

        Args:
            width: width.
            height: height.
            x: x
            y: y
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Retrive the size of the rectangle.

        Returns:
            The width of the retangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the retangle.

        Args:
            value: The size of value to set.
        """
        self.__width = value

    @property
    def height(self):
        """
        Retrive the height of the rectangle.

        Returns:
            The height of the retangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set height of the retangle.

        Args:
            value: The size of value to set.
        """
        self.__height = value

    @property
    def x(self):
        """
        Retrive the x of the rectangle.

        Returns:
            The x value of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x of the rectangle.

        Args:
            value: The x value to set.
        """
        self.__x = value

    @property
    def y(self):
        """
        Retrive the y of the rectangle.

        Returns:
            The y value of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y of the rectangle.

        Args:
            value: The y value to set.
        """
        self.__y = value
