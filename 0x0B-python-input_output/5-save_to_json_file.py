#!/usr/bin/python3
"""writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """You must use the with statement
       You don’t need to manage exceptions
    """
    with open(filename, mode='w', encoding='utf-8')as f:
        json.dump(my_obj, f)
