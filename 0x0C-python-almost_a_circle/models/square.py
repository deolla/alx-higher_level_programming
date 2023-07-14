#!/usr/bin/python3
"""
This is a class Square that inherits from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialise a square instance.

        Args:
            size(int): size of square.
            x(int): size of x.
            y(int): size of y.
            id: unique number.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Retrive the size of the square.

        Returns:
            return the size of a square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value: The size of the value to set.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attributes.

        Args:
            args: no-keyworded arguments.
            kwargs: keyworded arguments.
        """
        arg_cunt = len(args)
        if arg_cunt > 0:
            self.id = args[0]
        if arg_cunt > 1:
            self.size = args[1]
        if arg_cunt > 2:
            self.x = args[2]
        if arg_cunt > 3:
            self.y = args[3]
        if arg_cunt == 0 or len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns:
            returns the dictionary representation of a Square.
        """
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
        }

    def __str__(self):
        """
        Returns:
            return [Square] (<id>) <x>/<y> - <size>.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
