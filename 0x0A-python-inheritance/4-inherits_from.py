#!/usr/bin/python3
"""Python class inheritance"""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance of a class
       that inherited (directly or indirectly) from the specified class;
       otherwise False
    """

    if issubclass(obj, a_class) and obj != a_class:
        return True
    else:
        return False
