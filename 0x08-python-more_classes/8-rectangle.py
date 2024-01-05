#!/usr/bin/python3

''' Docstring to create a python class'''


class Rectangle:
    """

    An empty Rectangle class

    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle"""

        type(self).number_of_instances += 1
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
            [draw.append(str(self.print_symbol)) for j in range(self.__width)]

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

        then an instance of Rectangle is deleted
        """

        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """method that returns the biggest rectangle based on the area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
