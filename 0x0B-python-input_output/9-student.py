#!/usr/bin/python3
"""
A class student
"""


class Student:
    """
    a class Student that defines a student
    """
    def __init__(self. first_name, last_name, age):
        """
        initialising student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Method that returns directory description """
        return self.__dict__.copy()
