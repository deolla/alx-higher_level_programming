#!/usr/bin/python3

"""
This is a class Square that defines a square.
"""


class Square:
    """
    This class represents a sqaure.

    Attributes:
        __size (int): The size of sqaure.
        __position (tuple): The positiom of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialises a square instance with an optional size.

        Args:
            size (int): The size of the sqaure. Default to 0.

        Raises:
            TypeError: If size is not an integer,
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter method for the position attribute.

        Returns:
            tuples: The position of the sqaure.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute.

        Args:
            values (tuple): The position of the square.

        Raises:
            TypeError: If values is not tuples of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculate the return of the area of the square.

        Returns:
            int: The area of square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' in stdout.

        if size is equal to 0, print an empty line.
        The position is used to determine the starting position of the square.

        Returns:
            None
        """
        if self.__size == 0:
            print()
            return

            for i in range(self.__position[1]):
                print()

            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        square_str = ""

        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for m in range(0, self.__position[0])]
            [print("#", end="") for p in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
