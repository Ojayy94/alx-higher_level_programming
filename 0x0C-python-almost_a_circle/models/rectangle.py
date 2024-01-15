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
