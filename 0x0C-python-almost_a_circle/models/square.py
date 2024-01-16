#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """clas constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overloading __str__ method should return [Square] (<id>)
           <x>/<y> - <size> - in our case, width or height
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """width parameter"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """adding the public method that assigns attributes"""
        arg = len(args)
        kwarg = len(kwargs)
        attributes = ['id', 'size', 'x', 'y']

        f arg > 4:
            arg = 4

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
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
