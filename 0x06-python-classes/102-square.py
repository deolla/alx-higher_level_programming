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
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the size of the sqaure.

        Returns:
            int: The size of the sqaure.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size of value to set.

        Raises:
            TypeError: If size is not am integer.
            ValueError: If size must be >= 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate the return of the area of the square.

        Returns:
            int: The area of square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compares the square area with another square area for equality.

        Args:
            other (Square): Another square object.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Compares the square area with another square area for inequality.

        Args:
            other (Square): Another square object.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        Compares the square area with another square area for greater than.

        Args:
            other (Square): Another square object.

        Returns:
            bool: True if the area is greater, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """
        Compares the square area with another square area.

        Args:
            other (Square): Another square object.

        Returns:
            bool: True if the area is greater than or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __lt__(self, other):
        """
        Compares the square area with another square area for less than.

        Args:
            other (Square): Another square object.

        Returns:
            bool: True if the area is less, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """
        Compares the square area with another square
        area for less than or equal to.

        Args:
            other (Square): Another square object.

        Returns:
            bool: True if the area is less than or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False
