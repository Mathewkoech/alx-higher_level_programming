#!/usr/bin/python3
"""Defines test cases for base class"""
import sys
import os
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

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()


class Test_Base_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_file_more_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 2)

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()


class Test_Base_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""
    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_type(self):
        input = [{"id": 70, "width": 15, "height": 14}]
        json_input = Rectangle.to_json_string(input)
        list_expected_output = Rectangle.from_json_string(json_input)
        self.assertEqual(list, type(list_expected_output))


class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """removing any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rectangle(self):
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as file:
            self.assertTrue("5,1,2,3,4", file.read())

    def test_save_to_file_csv_one_square(self):
        s = Square(1, 2, 4, 5)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("5,1,2,4", f.read())

    def test_save_to_file_csv_with_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """removing any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 11)


if __name__ == "__main__":
    unittest.main()
