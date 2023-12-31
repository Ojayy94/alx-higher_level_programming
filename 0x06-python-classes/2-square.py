#!/usr/bin/python3

"""Write a class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize the new Square"""

        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
