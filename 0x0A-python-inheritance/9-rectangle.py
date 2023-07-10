#!/usr/bin/python3

"""
A class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry.

    Attribute:
        width: width of the rectangle.
        height: height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Instantiation width and height.
        """
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height

    def area(self):
        """
        Returns:
            int: The area of rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns:
            rectangle description: [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
