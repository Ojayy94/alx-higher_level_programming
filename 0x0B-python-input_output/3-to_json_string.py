#!/usr/bin/python3
"""JSON representation of an object (string)"""
import json
from json import dumps


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string):"""

    return json.dumps(my_obj)
