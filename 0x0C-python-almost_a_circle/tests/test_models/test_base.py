#!/usr/bin/python3
"""To test different behaviors of the Base class"""
import unittest
import pep8
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """To test the Base Class"""
    def test_pep8_base(self):
        """To check PEP8"""
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/base.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Checks: Found code style errors (and warnings)."
        )

    def test_float_id(self):
        """Test for float"""
        base_instance = Base(6.4)
        self.assertEqual(base_instance.id, 6.4)
        base_instance = Base(5.4)
        self.assertEqual(base_instance.id, 5.4)

    def test_id_as_positive(self):
        """Test for a positive Base Class id"""
        base_instance = Base(145)
        self.assertEqual(base_instance.id, 145)
        base_instance = Base(58)
        self.assertEqual(base_instance.id, 58)

    def test_id_as_negative(self):
        """Test for a negative Base Class id"""
        base_instance = Base(-79)
        self.assertEqual(base_instance.id, -79)
        base_instance = Base(-6)
        self.assertEqual(base_instance.id, -6)

    def test_complex_id(self):
        """Test complex cases"""
        base_instance = Base(complex(8))
        self.assertEqual(base_instance.id, complex(8))
        base_instance = Base(complex(5))
        self.assertEqual(base_instance.id, complex(5))

    def test_id_as_none(self):
        """Test None Base Class id"""
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)
        base_instance = Base(None)
        self.assertEqual(base_instance.id, 2)

    def test_tuple_id(self):
        """Test tuple methos in Class id"""
        base_instance = Base((1, 2, 3, 4))
        self.assertEqual(base_instance.id, (1, 2, 3, 4))

    def test_range_id(self):
        """Test range"""
        base_instance = Base(range(5))
        self.assertEqual(base_instance.id, range(5))

    def test_set_id(self):
        """Test set method"""
        base_instance = Base({1, 2, 3})
        self.assertEqual(base_instance.id, {1, 2, 3})

    def test_string_id(self):
        """Test String Class id"""
        base_instance = Base('ALX Higher Level')
        self.assertEqual(base_instance.id, 'ALX Higher Level')
        base_instance = Base('Almost a circle')
        self.assertEqual(base_instance.id, 'Almost a circle')

    def test_bool_id(self):
        """Test Boolean"""
        base_instance = Base(True)
        self.assertEqual(base_instance.id, True)
        base_instance = Base(False)
        self.assertEqual(base_instance.id, False)

    def test_list_id(self):
        """Test lists"""
        base_instance = Base([1, 2, 3, 4])
        self.assertEqual(base_instance.id, [1, 2, 3, 4])

    def test_inf_id(self):
        """Infinity test Case"""
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        """NaN test case"""
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        """Test two base case"""
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_to_json_string(self):
        """Test to_json_string method"""
        rect_instance = Rectangle(10, 7, 2, 8, 70)
        rect_data = re1.to_dictionary()
        json_data = Base.to_json_string([rect_data])
        self.assertEqual(type(json_data), str)

    def test_empty_to_json_string(self):
        """Test empty data on the to_json_string method"""
        empty = []
        json_data = Base.to_json_string(empty)
        self.assertEqual(json_data, "[]")

        empty = None
        json_data = Base.to_json_string(empty)
        self.assertEqual(json_data, "[]")

    def test_instance(self):
        """Test a Base Class instance"""
        base_instance = Base()
        self.assertEqual(type(base_instance), Base)
        self.assertTrue(isinstance(base_instance, Base))

    def test_to_json_string(self):
        """Test a normal to_json_string functionality"""
        rect_data = {'id': 31, 'x': 14, 'y': 11, 'width': 3, 'height': 3}
        json_data = Base.to_json_string([rect_data])

        self.assertTrue(isinstance(rect_data, dict))
        self.assertTrue(isinstance(json_data, str))
        self.assertCountEqual(
            json_data,
            '{["id": 31, "x": 14, "y": 11, "width": 3, "height": 3]}'
        )

    def test_wrong_to_json_string(self):
        """
        Test a wrong functionality of the
        to_json_string method
        """
        json_data = Base.to_json_string(None)
        self.assertEqual(json_data, "[]")

        warn = ("to_json_string() missing 1 required positional argument: " +
                "'list_dictionaries'")

        with self.assertRaises(TypeError) as msg:
            Base.to_json_string()

        self.assertEqual(warn, str(msg.exception))

        warn = "to_json_string() takes 1 positional argument but 2 were given"

        with self.assertRaises(TypeError) as msg:
            Base.to_json_string([{43, 87}], [{22, 17}])

        self.assertEqual(warn, str(msg.exception))

    def test_wrong_save_to_file(self):
        """
        Test the save_to_file method
        """
        with self.assertRaises(AttributeError) as msg:
            Base.save_to_file([Base(1), Base(2)])

        self.assertEqual(
             "'Base' object has no attribute 'to_dictionary'",
             str(msg.exception)
        )

if __name__ == "__main__":
    unittest.main()
