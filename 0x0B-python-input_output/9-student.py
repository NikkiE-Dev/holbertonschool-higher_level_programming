#!/usr/bin/python3
"""This module defines a class by students"""


class Student:
    """This class is defined by the public attr"""

    def __init__(self, first_name, last_name, age):
        """This is the instance attributes of the class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return {key: value for (key, value) in self.__dict__.items()
                if key in list(self.__dict__.keys())}
