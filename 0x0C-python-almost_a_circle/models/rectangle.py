#!/usr/bin/python3
"""Class rectangle that inherits from base"""
from models.base import Base


class Rectangle:
    """instances attributes"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width paerameter"""
        return self.__width

    @width.setter
    def width(self, value):
        """by adding validation of all setter methods and instantiation"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height parameter"""
        return self.__height

    @height.setter
    def height(self, value):
        """by adding validation of all setter methods and instantiation"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x parameter"""
        return self.__x

    @x.setter
    def x(self, value):
        """by adding validation of all setter methods and instantiation"""
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y parameter"""
        return self.__y

    @y.setter
    def y(self, value):
        """by adding validation of all setter methods and instantiation"""
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """that returns the area value of the Rectangle instance"""
        return (self.width * self.height)

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        if self.height == 0 or self.width == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for j in range(self.width)]
            print("")

    def __str__(self):
        """Update the class Rectangle by overriding the __str__ method so
           it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """pdate the class Rectangle by adding the public method"""
        arg = len(args)
        kwarg = len(kwargs)
        attributes = ['id', 'width', 'height', 'x', 'y']

        if arg > 5:
            arg = 5

        if arg > 0:
            for i in range(arg):
                setattr(self, attributes[i], args[i])

        elif kwarg > 0:
            for k, v in kwargs.items():
                if k in attributes:
                    setattr(self, k, v)

    def to_dictionary(self):
        """public attributes"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
