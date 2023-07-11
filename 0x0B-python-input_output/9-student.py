#!/usr/bin/python3
"""
Define the class Student.
"""


class Student:
    """
    a class Student that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialising student method.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns directory description
        """
        return self.__dict__.copy()
