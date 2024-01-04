#!/usr/bin/python3

''' Docstring to create a python class'''


class Rectangle:
    """

    An empty Rectangle class

    """

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Set height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of the Rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """Perimeter of the Rectangle"""

        if self.__width == 0 or self.__height == 0:
            return (0)

        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Printable representation of the Rectangle"""

        if self.__width == 0 or self.__height == 0:
            return ("")

        draw = []
        for i in range(self.__height):
            [draw.append('#') for index in range(self.__width)]

            if i != self.__height - 1:
                draw.append("\n")
        return "".join(draw)

    def __repr__(self):
        """string representation of the Rectangle"""

        draw = "Rectangle(" + str(self.__width)
        draw += ", " + str(self.__height) + ")"
        return draw

    def __del__(self):
        """
        Print the message Bye rectangle...
        (... being 3 dots not ellipsis)
        when an instance of Rectangle is deleted
        """

        print("Bye rectangle...)
