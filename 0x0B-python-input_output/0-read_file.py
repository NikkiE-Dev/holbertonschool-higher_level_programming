#!/usr/bin/python3
"""This module reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """This class defines the parameters of the function"""

    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read())
