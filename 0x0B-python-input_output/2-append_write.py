#!/usr/bin/python3
"""
This module appends a string at the end of a text file (UTF8)
& returns the number of characters added
"""


def append_write(filename="", text=""):
    """This class defines the parameters of the function"""

    fileString1 = len(text)
    with open(filename, mode="a", encoding="utf-8") as newFile:
        newFile.write(text)
    with open(filename, encoding="utf-8") as newFile:
        fileString2 = newFile.read()
    if fileString1 <= len(fileString2):
        return fileString1
    else:
        return len(fileString2) - fileString1
