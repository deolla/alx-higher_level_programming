#!/usr/bin/python3
""" 
Defines the class Student
"""


class Student:
    """
    Class student
    """

    def __init__(self, first_name, last_name, age):
        """
        Method to initialize
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method that returns directory description """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            lists = {}

            for i in range(len(attrs)):
                for s in obj:
                    if attrs[i] == s:
                        lists[s] = obj[s]
            return lists

        return obj
