#!/usr/bin/python3
"""This module creates an Object from a JSON file"""


import json


def load_from_json_file(filename):
    """This fuction calls with the filename"""

    with open(filename, mode='r') as newFile:
        fileString = newFile.read()
        jsonObject = json.loads(fileString)
        return jsonObject
