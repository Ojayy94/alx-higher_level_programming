#!/usr/bin/python3
"""Buiding a test model"""
import unittest
import pep8
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """To test the square model"""
    def test_pep8_base(self):
        """test that checks PEP8"""
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/square.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Checks: Found code style errors (and warnings)"
        )

    def test_empty(self):
        with self.assertRaises(TypeError):
            Square()
