#!/usr/bin/python3
"""This module defines a class by students"""


class Student:
    """This class is defined by the public attr"""

    def __init__(self, first_name, last_name, age):
        """This is the instance attributes of the class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return vars(self)

        else:
            newAttrs = {}
            if isinstance(attrs, list):
                for a in attrs:
                    if hasattr(self, a):
                        newAttrs[a] = getattr(self, a)
                return newAttrs

    def reload_from_json(self, json):
       for key in json:
           setattr(self, key, json[key])
       
