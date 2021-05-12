#!/usr/bin/python3
"""
This module reads a text file (UTF8)
& returns the number of characters written
"""


def write_file(filename="", text=""):
    """This class defines the parameters of the function"""

    with open(filename, mode="w", encoding="utf-8") as newFile:
        newFile.write(text)
    with open(filename, encoding="utf-8") as newFile:
        fileString = newFile.read()
        return len(fileString)
