#!/usr/bin/python3
"""Write a class"""


class Student:
    """student attributes"""
    def __init__(self, first_name, last_name, age):
        """create an object instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns the dictionary description with simple data structure"""
        return self.__dict__
