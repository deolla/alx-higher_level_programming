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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
         Initialise a rectangle instance with the given width and height.

         Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    def area(self):
        """
        Calculate the return of the area of rectangle.

        Returns:
            int: The area of rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the return of the perimeter of rectangle.

        Returns:
            int: The parameter of rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        Returns:
            the rectangle with the character #.
        """
        if self.width == 0 or self.height == 0:
            return ""
        rec_str = ""
        for _ in range(self.height):
            rec_str += str(self.print_symbol) * self.width + "\n"
        return rec_str[:-1]

    def __repr__(self):
        """
        Returns:
            a string representation of the rectangle.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Print the message when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area.

        Raises:
            TypeError:  If rect_1 is not Rectangle.
                        If rect_2 is not Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
