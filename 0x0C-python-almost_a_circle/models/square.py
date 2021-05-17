#!/usr/bin/python3
"""This module is for create a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This module is for Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.height)

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value
