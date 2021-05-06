#!/usr/bin/python3
""" This is how you create a module."""


class Square:
    """ This is how you create a simple class."""

    def __init__(self, size=0, position=(0, 0)):
        """This is how you create instantiation with size defined"""

        self.__position = position
        self.__size = size
        """This is how you create a private attribute in a class"""
        if not isinstance(position, tuple) or min(position) < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
        """Checks if size is an int & is greater than or equal to 0"""

    def area(self):
        """This is how you create a public instance method"""

        sq = self.__size * self.__size
        return(sq)
        """Calculating size squared and returning it"""
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or min(value) < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        for x in range(self.__position[1]):
            print()
            return
        for x in range(self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for x in range(self.__size):
                print("#", end="")
            print()
