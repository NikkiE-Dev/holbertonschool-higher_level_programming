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

    def update(self, *args, **kwargs):
        """Replacing items with updated args"""
        if len(args):
            for i, e in enumerate(args):
                if i == 0:
                    self.id = e
                if i == 1:
                    self.size = e
                if i == 2:
                    self.x = e
                if i == 3:
                    self.y = e

        elif kwargs is not None:
            for (a, b) in kwargs.items():
                if a == 'id':
                    self.id = b
                if a == 'size':
                    self.size = b
                if a == 'x':
                    self.x = b
                if a == 'y':
                    self.y = b

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
