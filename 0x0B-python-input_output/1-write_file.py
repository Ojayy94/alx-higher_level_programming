#!/usr/bin/python3
""" writes a string to a text file"""


def write_file(filename="", text=""):
    """You must use the with statement
        You don’t need to manage file permission exceptions
        Your function should create the file if doesn’t exist
        Your function should overwrite the content of the file
        if it already exists
        and returns the number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
