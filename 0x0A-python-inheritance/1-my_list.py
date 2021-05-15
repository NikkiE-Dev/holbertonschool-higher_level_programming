#!/usr/bin/python3
"""This module is to create a class that inherits from list"""


class MyList(list):
    """This is the class that we create"""

    def print_sorted(self):
        """This that prints the list, but sorted (ascending sort)"""

        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
