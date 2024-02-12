#!/usr/bin/python3
"""Defines test cases for base class"""
import sys
import json
import unittest
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instance(unittest.TestCase):

    def test_init_with_id(self):
        """
        Test initializing Base with provided id.
        """
        base = Base(10)
        self.assertEqual(base.id, 10)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_two_args(self):
        """Test initializing with two args"""
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_init_without_id(self):
        """
        Test initializing Base without id, generating new id.
        """
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id + 1, base2.id)

class TestBase_to_jsonstring(unittest.TestCase):

    def test_to_json_string_none(self):
        """
        Test to_json_string with None input.
        """
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_string_empty_list(self):
        """
        Test to_json_string with empty list.
        """
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_with_data(self):
        """
        Test to_json_string with list of dictionaries.
        """
        data = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
        json_string = Base.to_json_string(data)
        self.assertEqual(json.loads(json_string), data)

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_to_json_string_square_type(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

if __name__ == "__main__":
    unittest.main()
