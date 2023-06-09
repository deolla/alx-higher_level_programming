#!/usr/bin/python3

"""
A function that prints a messages
"""


def say_my_name(first_name, last_name=""):
    """
    Print the name with the format "My name is <first name> <last name>".

    Args:
        first_name (str): The first name.
        last_name (str): The last name (dafualt: "").

    Raises:
        TypeError: If first_name is not a string or last_name is not a string.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if last_name is None:
        raise TypeError("last_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
