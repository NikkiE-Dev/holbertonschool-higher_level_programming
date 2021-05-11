#!/usr/bin/python3
"""
This module that prevents the user from dynamically
creating new instance attributes,
except if the new instance attribute is called first_name
"""


class LockedClass():
    """This is a class with no class or object attribute"""

    __slots__ = 'first_name'
