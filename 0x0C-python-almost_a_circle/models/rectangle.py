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

    @property
    def height(self):
        """height parameter"""
        return self.__height

    @property
    def x(self):
        """x parameter"""
        return self.__x

    @property
    def y(self):
        """y parameter"""
        return self.__y
