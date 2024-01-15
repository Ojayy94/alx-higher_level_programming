#!/usr/bin/python3
"""creating a base class"""
import json
import os


class Base:
    """private class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """if id is not None, assign the public instance attribute id
           with this argument value - you can assume id is an integer
           and you don’t need to test the type of it

           otherwise, increment __nb_objects and assign the new value
           to the public instance attribute id
        """

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Update the class Base by adding the static method"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        filename = cls.__name__ + '.json'
        with open(filename, mode='w', encoding='utf-8') as file:
            if list_objs is None:
                file.write('[]')
            else:
                list_dicts = [i.to_dictionary() for i in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == []:
            return '[]'
        return json.loads(json_string)
