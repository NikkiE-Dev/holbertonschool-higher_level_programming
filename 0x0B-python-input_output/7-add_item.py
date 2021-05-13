#!/usr/bin/python3
"""This module creates an Object from a JSON file"""


import json, sys, os
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


if __name__ == "__main__":
    """Takes line args and adds them to a JSON file"""

    newList = []
    newFile = "add_item.json"

    if os.path.exists(newFile):
        if os.path.getsize(newFile) is not 0:
            newList.extend(load_from_json_file(newFile))
    else:
        p = open(newFile, "x")
        p.close()
    for a in range(1, len(sys.argv)):
        newList.append(sys.argv[a])
    save_to_json_file(newList, newFile)
