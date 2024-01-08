#!/usr/bin/python3
"""class"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """raise Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if type(value) <= 0:
            raise ValueError("{} must be greater than 0".format(name))
