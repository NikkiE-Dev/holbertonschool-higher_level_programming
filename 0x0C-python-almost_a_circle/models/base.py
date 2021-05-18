#!/usr/bin/python3
"""This module is for Unittest is for Base"""
import json


class Base:

    """This is the base for the rectangle"""

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or ():
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or ():
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dumm_list = cls(2, 1)
        dumm_list.update(**dictionary)
        return dumm_list

    @classmethod
    def save_to_file(cls, list_objs):
        """Adding the class method that writes
        the JSON string representation of list_objs to a file
        """
        nw_lst = []
        cls_name = cls.__name__
        if list_objs is None:
            wrt = cls.to_json_string(nw_lst)
            with open(cls_name + '.json', 'w', encoding='utf-8') as newFile:
                newFile.write(wrt)
            return
        for item in list_objs:
            if issubclass(type(item), Base):
                nw_lst.append(item.to_dictionary())
        wrt = cls.to_json_string(nw_lst)
        with open(cls_name + '.json', 'w', encoding='utf-8') as newFile:
            newFile.write(wrt)
