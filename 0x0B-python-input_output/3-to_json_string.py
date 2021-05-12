#!/usr/bin/python3
"""
This module returns the JSON
representation of an object (string)
"""

import json


def to_json_string(my_obj):
    """This class defines the parameters of the function"""

    return json.dumps(my_obj)
