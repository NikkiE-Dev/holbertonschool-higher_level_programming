#!/usr/bin/python3
"""This module is to create a class that inherits from list"""


def is_same_class(obj, a_class):
    """"Checks to see if the obj is exactly an instance of the specific class"""

    if (type(obj) == a_class):
        return True
    else:
        return False
