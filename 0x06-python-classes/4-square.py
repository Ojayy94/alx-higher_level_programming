#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """Private instance attribute: size"""

    def __init__(self, size=0):
        """size must be an integer, otherwise raise a TypeError exception
            with the message size must be an integer
            if size is less than 0, raise a ValueError exception with
            the message size must be >= 0
            Public instance method: def area(self): that returns
            the current square area"""

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
