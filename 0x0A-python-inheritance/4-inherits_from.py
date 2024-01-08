#!/usr/bin/python3
"""Python class inheritance"""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance of a class
       that inherited (directly or indirectly) from the specified class;
       otherwise False
    """

    if isinstance(obj, a_class) and issubclass(a_class, obj.__class__)\
       is False:
        return True
    else:
        return False
