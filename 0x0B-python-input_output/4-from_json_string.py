#!/usr/bin/python3
"""
This module returns the python data structure
represented by a JSON string
"""

import json


def from_json_string(my_str):
    """This class defines the parameters of the function"""

    return json.loads(my_str)
