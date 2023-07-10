#!/usr/bin/python3
"""
A class MyInt that inherits from int
"""


class MyInt(int):
    """
    A class representing a rebellious integer
    """
    def __eq__(self, other):
        """
        Overrides the == operator
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator
        """
        return super().__eq__(other)
