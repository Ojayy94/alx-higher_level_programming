#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square:
    """Class Square inherits from Rectangle"""
    def def __init__(self, size, x=0, y=0, id=None):
        """clas constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overloading __str__ method should return [Square] (<id>)
           <x>/<y> - <size> - in our case, width or height
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)
