#!/usr/bin/python3
"""
This module has a name
where both first and last
have to be a string
"""


def say_my_name(first_name, last_name=""):
    """This function prints first name and last name"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
