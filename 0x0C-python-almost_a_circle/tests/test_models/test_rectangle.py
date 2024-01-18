#!/usr/bin/python3
"""To test different behaviors of the Base class"""
import unittest
import pep8
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """To test the Rectangle Class"""
    def test_pep8_base(self):
        """To check PEP8"""
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/base.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Checks: Found code style errors (and warnings)."
        )

    def test_width_private(self):
        """To test the Rectangle instance"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_setter(self):
        """To test the Rectangle instance"""
        r = Rectangle(5, 5, 0, 0, 1)
        r.width = 10
        self.assertEqual(10, r.width)
        r.height = 10
        self.assertEqual(10, r.height)
        r.x = 10
        self.assertEqual(10, r.x)
        r.y = 10
        self.assertEqual(10, r.y)

    def test_height_private(self):
        """To test the Rectangle instance"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_no_args(self):
        """Test if Rectangle has no argument"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """Test if Rectangle takes argument"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_rectangle_subclass(self):
        """Test if Rectangle class inherit from Base class"""
        self.assertFalse(issubclass(Rectangle, Base))

    def test_string_id(self):
        """To test the Rectangle string case"""
        with self.assertRaises(TypeError):
            Rectangle('Monty', 'Python')

    def test_more_args(self):
        """Test if Rectangle takes argument"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_type(self):
        """Test if Rectangle takes type argument"""
        with self.assertRaises(TypeError):
            Rectangle(True, 7)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 2.1)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(1, "Hello")
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(4.41, 5.3)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(-13, 14)
            raise ValueError()

if __name__ == "__main__":
    unittest.main()
