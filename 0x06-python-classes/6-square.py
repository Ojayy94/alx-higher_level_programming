#!/usr/bin/python3

"""Write a class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """Square Class a Square Class"""

    def __init__(self, size=0, position=(0, 0)):
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

        if self.__check_tuple(position) is False \
           or self.__check_indexes(position) is False \
           or self.__check_integers(position) is False \
           or self.__check_values(position) is False:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        """The size setter method update the size value of the square.

        Attributes:
            size (:obj:`int`): The new size of the square.

        Raises:
            TypeError: If `size` type is not `int`.

            ValueError: If `size` is less than `0`."""

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if self.__check_tuple(position) is False \
           or self.__check_indexes(position) is False \
           or self.__check_integers(position) is False \
           or self.__check_values(position) is False:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position

    def __check_tuple(self, position):
        if type(position) is tuple:
            return True

        return False

    def __check_indexes(self, position):
        if len(position) == 2:
            return True

        return False

    def __check_integers(self, position):
        if type(position[0]) is int and type(position[1]) is int:
            return True

        return False

    def __check_values(self, position):
        if position[0] >= 0 and position[1] >= 0:
            return True

        return False

    def area(self):
        """Returns the current square area"""

        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return None

        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print('')

        for j in range(1, self.area() + 1):
            if j % self.__size == 1:
                print('{:>{w}}'.format('#', w=self.__position[0] + 1), end='')
            else:
                print('#', end='')

            if j % self.__size == 0 and j > 0:
                print()
