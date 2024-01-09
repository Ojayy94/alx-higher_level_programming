#!/usr/bin/python3
"""Write a class"""


class Student:
    """student attributes"""
    def __init__(self, first_name, last_name, age):
        """create an object instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dictionary description with simple data structure"""
        cls_d = self.__dict__
        my_d = dict()

        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    return cls_d

                if attr in cls_d:
                    my_d[attr] = cls_d[attr]

            return my_d

        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student"""
        for k, v in json.items():
            setattr(self, k, v)
