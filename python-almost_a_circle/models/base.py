#!/usr/bin/python3
"""
class base
"""

import json


class Base:
    """ Doc """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return JSON string of list dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs """
        filename = type(list_objs[0]).__name__ + "Rectangle.json"
        json_file = open(filename, "w")
        if list_objs is None:
            json.dump([], json_file)

        if type(list_objs[0]).__name__ == "Rectangle":
            new_dict = [item.to_dictionary() for item in list_objs]
            json_string = cls.to_json_string(new_dict)
            json.dump(new_dict, json_file)

        json_file.close()
