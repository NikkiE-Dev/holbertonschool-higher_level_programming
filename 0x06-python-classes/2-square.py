#!/usr/bin/python3
""" This module is how you create a class."""


class Square:
    """ This is how you create a simple class."""
    def __init__(self, size=0):
        """This is how you create a private attribute in a class"""
        self.__size = size
        """Checks if size is an int & is greater than or equal to 0"""

        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
