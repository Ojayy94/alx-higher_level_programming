#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    """You must use the with statement
        You don’t need to manage file permission or
        file doesn't exist exceptions
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end = "")
