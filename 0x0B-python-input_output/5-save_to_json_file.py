#!/usr/bin/python3
"""
This module returns the python data structure
represented by a JSON string
"""

import json


def save_to_json_file(my_obj, filename):
    """This class defines the parameters of the function"""

    with open(filename, mode='w', encoding="utf-8") as newFile:
        return newFile.write(json.dumps(my_obj))
