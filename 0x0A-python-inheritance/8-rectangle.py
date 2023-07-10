#!/usr/bin/python3

"""
subclass rectangle
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
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height
