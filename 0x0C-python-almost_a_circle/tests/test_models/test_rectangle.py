#!/usr/bin/python3
"""Defines unittests for models/rectangle.py"""


from io import StringIO
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_rectangle_validation(unittest.TestCase):
    """testing rectangle validation"""
    def test_width_validation(self):
        """test height validation"""
        with self.assertRaises(TypeError) as context:
            r = Rectangle("num", 2)
        self.assertEqual(str(context.exception), "width must be an integer")

        with self.assertRaises(ValueError) as context:
            r = Rectangle(-2, 7)
            self.assertEqual(str(context.exception), "width must be > 0")

    def test_height_validation(self):
        """test height validation"""
        with self.assertRaises(TypeError) as context:
            r = Rectangle(2,"num")
        self.assertEqual(str(context.exception), "height must be an integer")

        with self.assertRaises(ValueError) as context:
            r = Rectangle(3, -2)
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_x_validation(self):
        """test x validation"""
        with self.assertRaises(TypeError) as context:
            r = Rectangle(2, 4, "num", 1)
        self.assertEqual(str(context.exception), "x must be an integer")

        with self.assertRaises(ValueError) as context:
            r = Rectangle(2, 4, -1, 1)
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_y_validation(self):
        """test y validation"""
        with self.assertRaises(TypeError) as context:
            r = Rectangle(2, 4, 1, "num")
        self.assertEqual(str(context.exception), "y must be an integer")

        with self.assertRaises(ValueError) as context:
            r = Rectangle(2, 4, 2, -2)
        self.assertEqual(str(context.exception), "y must be >= 0")

class TestRectangleArea(unittest.TestCase):
    def test_area_with_positive_dimensions(self):
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

    def test_area_with_zero_dimensions(self):
        rect = Rectangle(0, 0)

class TestRectangleDisplay(unittest.TestCase):
    def setUp(self):
        # Redirect stdout to capture print statements
        self.saved_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        # Restore original stdout
        sys.stdout = self.saved_stdout

    def test_display_with_positive_dimensions(self):
        r = Rectangle(2, 2)
        r.display()
        printed_output = sys.stdout.getvalue()
        expected_output = "##\n##\n"
        self.assertEqual(printed_output, expected_output)

    def test_display_with_zero_dimensions(self):
        r = Rectangle(0, 0)
        r.display()
        printed_output = sys.stdout.getvalue()
        expected_output = "\n"
        self.assertEqual(printed_output, expected_output)

    def test_display_with_negative_dimensions(self):
        r = Rectangle(-2, -2)
        r.display()
        printed_output = sys.stdout.getvalue()
        expected_output = "##\n##\n"
        self.assertEqual(printed_output, expected_output)

class TestRectangleStrMethod(unittest.TestCase):

    def test_str_method(self):
        r = Rectangle(1, 2, 3, 4, 5)
        expected_output = "[Rectangle] (5) 3/4 - 1/2"
        self.assertEqual(str(r), expected_output)


class TestRectangleUpdateMethod(unittest.TestCase):

    def test_update_with_invalid_args(self):
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "id must be an integer"):
            r.update("num", 3, 4, 5, 6)

    def test_update_with_negative_values(self):
        r = Rectangle(-1, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(2, -2, 4, 5, 6)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(2, 3, -3, 5, 6)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(2, 3, 4, -6, 6)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(2, 3, 4, 5, -9)

    def test_update_with_too_few_args(self):
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.update(2)

    def test_update_with_args(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(2, 3, 4, 5, 6)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    def test_update_with_kwargs(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(id=2, width=3, height=4, x=5, y=6)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    def test_update_with_args_and_kwargs(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(2, 3, 4, 5, 6, id=7, width=8, height=9, x=10, y=11)
        self.assertEqual(r.id, 2)  # takes previous
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

class test_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Rectangle class."""
    def test_rectangle_to_dictionary(self):
        r = Rectangle(1, 2, 3, 4, 5)
        expected_result = {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        self.assertEqual(r.to_dictionary(), expected_result)



if __name__ == "__main__":
    unittest.main()
