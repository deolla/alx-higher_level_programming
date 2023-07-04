#!/usr/bin/python3
"""
This is a class LockedClass
"""


class LockedClass:
    """
    A class LockedClass with no class or object attribute.
    """
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        """
        Creating new instance.

        Args:
            name: The name of the attribute being set.
            value: The value being assigned to that attribute.

        Raises:
            AttributeError: if object has no attribute.
        """
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no"
            " attribute '{}'".format(name))
        object.__setattr__(self, name, value)
