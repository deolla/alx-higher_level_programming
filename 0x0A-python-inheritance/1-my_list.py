#!/usr/bin/python3
"""
This is a class MyList that inherits from list.
"""


class MyList(list):
    """
    Public instance method
        prints the list, but sorted (ascending sort).
    """
    def print_sorted(self):
        """
            Prints the list, but sorted (ascending sort)
        """
        sorted_list = sorted(self)
        print(sorted_list)
