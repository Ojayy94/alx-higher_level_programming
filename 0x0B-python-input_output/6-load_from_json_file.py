#!/usr/bin/python3
"""creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """You must use the with statement"""
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
