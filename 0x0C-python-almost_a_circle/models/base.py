#!/usr/bin/python3

"""
This class will be the “base” of all other classes in this project.
"""


class Base:
    """
    This class is "base" of all classes in this project.

    Attribute:
        __nb_object: private class attribute.
        id:  public instance attribute.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialise the "base" instance with an optional id.

        Args:
            id (int): This is a unique identifier of the base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
