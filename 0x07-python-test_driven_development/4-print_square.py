#!/usr/bin/python3
"""
In this module size is the size length of the square
size must be an integer, size is less than 0,
and that size is not a comionation of
a float and is less than 0.
"""


def print_square(size):
    """This is how you create instantiation with size defined"""

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
            raise TypeError("size must be an integer")

    if size < 0:
        """Checks if size is an int & is greater than or equal to 0"""
        raise ValueError("size must be >= 0")
        for x in range(0, size):
        print(size * "#")
