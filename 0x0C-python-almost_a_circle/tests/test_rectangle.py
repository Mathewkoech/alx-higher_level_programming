#!/usr/bin/python3
"""Defines unittests for models/rectangle.py"""


import io
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
            r = Rectangle(2, "num")
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
    """unittest for area calculation"""

    def test_area_with_positive_dimensions(self):
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

    def test_area_one_arg(self):
        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)


"""class TestRectangleDisplay(unittest.TestCase):
    unittest for display # characters

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
        r = Rectangle(2, 3)
        r.display()
        printed_output = sys.stdout.getvalue()
        expected_output = "##\n##\n##\n"
        self.assertEqual(printed_output, expected_output)"""


class TestRectangle_stdout(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Rectangle class."""

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout.

        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    # Test __str__ method
    def test_str_method_print_width_height(self):
        r = Rectangle(4, 6)
        capture = TestRectangle_stdout.capture_stdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_width_height_x(self):
        r = Rectangle(5, 5, 1)
        correct = "[Rectangle] ({}) 1/0 - 5/5".format(r.id)
        self.assertEqual(correct, r.__str__())

    def test_str_method_width_height_x_y(self):
        r = Rectangle(1, 8, 2, 4)
        correct = "[Rectangle] ({}) 2/4 - 1/8".format(r.id)
        self.assertEqual(correct, str(r))

    def test_str_method_width_height_x_y_id(self):
        r = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))

    def test_str_method_changed_attributes(self):
        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

    def test_str_method_one_arg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

    # Test display method
    def test_display_width_height(self):
        r = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_width_height_x(self):
        r = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_width_height_y(self):
        r = Rectangle(4, 5, 0, 1, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_width_height_x_y(self):
        r = Rectangle(2, 4, 3, 2, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)


class TestRectangleStrMethod(unittest.TestCase):
    """unittest for string representation"""

    def test_str_method(self):
        r = Rectangle(1, 2, 3, 4, 5)
        expected_output = "[Rectangle] (5) 3/4 - 1/2"
        self.assertEqual(str(r), expected_output)


class TestRectangleUpdateMethod(unittest.TestCase):
    """unittest for updating rect dimensions"""

    def test_update_args_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(19, 1, 2, 3, -6)

    def test_update_with_negative_values(self):
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(2, -2, 4, 5, 6)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(2, 3, -3, 5, 6)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(2, 3, 4, -6, 6)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(2, 3, 4, 5, -9)

    def test_update_kwargs_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_update_args_height_zero(self):
        r = Rectangle(11, 11, 11, 11, 11)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(19, 1, 0)

    def test_update_kwargs_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_args_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_args_invalid_width_type(self):
        r = Rectangle(7, 7, 7, 7, 7)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(19, "num")

    def test_update_args_invalid_x_type(self):
        r = Rectangle(11, 11, 11, 11, 11)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(19, 2, 3, "num")

    def test_update_twice_kwargs(self):
        r = Rectangle(11, 11, 11, 11, 11)
        r.update(id=19, x=1, height=2)
        r.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (19) 1/3 - 2/15", str(r))

    def test_update_kwargs_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="num")

    def test_update_kwargs_with_zero_height(self):
        r = Rectangle(11, 11, 11, 11, 11)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_args_and_kwargs(self):
        r = Rectangle(11, 11, 11, 11, 11)
        r.update(19, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (19) 11/11 - 2/11", str(r))


class test_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Rectangle class."""
    def test_rectangle_to_dictionary(self):
        r = Rectangle(1, 2, 3, 4, 5)
        expected_result = {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        self.assertEqual(r.to_dictionary(), expected_result)

    def test_to_dictionary_arg(self):
        r = Rectangle(11, 2, 3, 1, 5)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
