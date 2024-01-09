#!/usr/bin/python3
""" appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """You must use the with statement
       If the file doesn’t exist, it should be created
       returns the number of characters added
    """
    with open(filename, mode='a', encodin='utf-8') as f:
        return f.write(text)
