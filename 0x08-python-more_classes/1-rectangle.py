#!/usr/bin/python3

''' Docstring to create a python class'''


class Rectangle:
    """

    An empty Rectangle class

    """

    def __init__(self, width=0, height=0):
        ''' Create an instance '''

        self.width = width
        self.height = height

        @property
        def width(self):
            ''' set rectangle width '''

            return self.__width

        @width.setter
        def width(self, value):
            ''' set width value '''

            if value not int:
                raise TypeError("width must be an integer")

            if value < 0:
                raise ValueError("width must be >= 0")
                self.__width = value

        @property
        def height(self):
            ''' set rectangle height '''

            return self.__height

        @width.setter
        def height(self, value):
            ''' set width value '''

            if value not int:
                raise TypeError("height must be an integer")

            if value < 0:
                raise ValueError("height must be >= 0")
                self.__height = value
