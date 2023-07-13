#!/usr/bin/python3

"""
This is a class Rectangle that inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """
    A class Rectangle that inherits from Base.

    Attributes:
        __width (int): width of the retangle.
        __height (int): height of the rectangle.
        __x (int): private attributes.
        __y (int): private attributes.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialises a rectangle instance.

        Args:
            width (int): width.
            height (int): height.
            x (int): x
            y (int): y
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
            value: The width of value to set.

        Raises:
            TypeError: width not integer.
            ValueError: value < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
            value: The height of value to set.

        Raises:
            TypeError: height not int.
            ValueError: value < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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

        Raises:
            TypeError: x not an integer.
            ValueError: value < 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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

        Raises:
            TypeError: y not an integer.
            ValueError: value < 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate the return of the area of the rectangle.

        Returns:
            int: The area of rectangle.
        """
        return self.height * self.width

    def display(self):
        """
        Prints in stdout the Rectangle instance with the character #.
        """
        output = ""
        for _ in range(self.y):
            output += "\n"
        for _ in range(self.height):
            output += " " * self.x + "#" * self.width + "\n"
        print(output, end="")

    def __str__(self):
        """
        Overriding the __str__ method.

        Returns:
            return [Rectangle] (<id>) <x>/<y> - <width>/<height>.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute.

        Args:
            args: no-keyword argument.
            kwargs: key-worded argument.
        """
        arg_cunt = len(args)
        if arg_cunt == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            if arg_cunt > 0:
                self.id = args[0]
            if arg_cunt > 1:
                self.width = args[1]
            if arg_cunt > 2:
                self.height = args[2]
            if arg_cunt > 3:
                self.x = args[3]
            if arg_cunt > 4:
                self.y = args[4]
