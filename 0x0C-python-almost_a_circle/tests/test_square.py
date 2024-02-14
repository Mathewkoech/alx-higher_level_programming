#!/usr/bin/python3
"""Defines unittests for models/square.py"""

import sys
import unittest
from models.base import Base
from models.square import Square
from io import StringIO
sys.stdout = StringIO()


class Test_square_validation(unittest.TestCase):
    """testing square validation"""
    def test_width_validation(self):
        """test width validation"""
        with self.assertRaises(TypeError) as context:
            s = Square("num", 2)
            self.assertEqual(str(context.exception),
                             "width must be an integer")

        with self.assertRaises(ValueError) as context:
            s = Square(-2, 7)
            self.assertEqual(str(context.exception), "width must be > 0")

    def test_x_validation(self):
        """test x validation"""
        with self.assertRaises(TypeError) as context:
            s = Square(4, "num", 1)
        self.assertEqual(str(context.exception), "x must be an integer")

        with self.assertRaises(ValueError) as context:
            s = Square(4, -1, 1)
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_y_validation(self):
        """test y validation"""
        with self.assertRaises(TypeError) as context:
            s = Square(4, 1, "num")
        self.assertEqual(str(context.exception), "y must be an integer")

        with self.assertRaises(ValueError) as context:
            s = Square(4, 2, -2)
        self.assertEqual(str(context.exception), "y must be >= 0")


class TestSquareArea(unittest.TestCase):
    """unittest for area calculation"""

    def test_area_with_positive_dimensions(self):
        s = Square(40, 5, 6)
        self.assertEqual(s.area(), 1600)


class TestSquareDisplay(unittest.TestCase):
    """unittest for display # characters"""

    def setUp(self):
        # Redirect stdout to capture print statements
        self.saved_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        # Restore original stdout
        sys.stdout = self.saved_stdout

    def test_display_with_positive_dimensions(self):
        s = Square(2, 3, 3)
        s.display()
        printed_output = sys.stdout.getvalue()
        expected_output = "\n\n\n   ##\n   ##\n"
        self.assertEqual(printed_output, expected_output)

    def test_display_with_zero_dimensions(self):
        r = Square(0, 0)
        r.display()
        printed_output = sys.stdout.getvalue()
        expected_output = ""
        self.assertEqual(printed_output, expected_output)

    def test_display_with_negative_dimensions(self):
        r = Square(2, 2)
        r.display()
        printed_output = sys.stdout.getvalue()
        expected_output = '  ##\n  ##\n'
        self.assertEqual(printed_output, expected_output)


class TestSquareStrMethod(unittest.TestCase):
    """unittest for string representation"""

    def test_str_method(self):
        s = Square(1, 2, 3, 4)
        expected_output = "[Square] (4) 2/3 - 1"
        self.assertEqual(str(s), expected_output)


class TestSquareUpdateMethod_args(unittest.TestCase):
    """unittest for updating square dimensions"""

    def test_update_zero_args(self):
        s = Square(5, 5, 5, 5)
        s.update()
        self.assertEqual("[Square] (5) 5/5 - 5", str(s))

    def test_update_args_invalid_type(self):
        s = Square(10, 7, 11, 9)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(19, "num")

    def test_update_args_size_zero(self):
        s = Square(10, 11, 12, 13)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(12, 0)

    def test_update_args_negative(self):
        s = Square(11, 9, 12, 13)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(28, -3)


class TestSquare_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of Square class."""

    def test_update_one_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(s))

    def test_update_kwargs_two(self):
        s = Square(10, 10, 10, 10)
        s.update(size=1, id=2)
        self.assertEqual("[Square] (2) 10/10 - 1", str(s))

    def test_update_three_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(y=1, size=3, id=33)
        self.assertEqual("[Square] (33) 10/1 - 3", str(s))

    def test_update_with_four_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(id=79, x=1, y=3, size=4)
        self.assertEqual("[Square] (79) 1/3 - 4", str(s))

    def test_update_kwargs_width_setter(self):
        s = Square(9, 9, 9, 9)
        s.update(id=19, size=9)
        self.assertEqual(9, s.width)

    def test_update_kwargs_height_setter(self):
        s = Square(11, 11, 12, 14)
        s.update(id=19, size=9)
        self.assertEqual(9, s.height)

    def test_update_kwargs_None_id(self):
        s = Square(9, 9, 9, 9)
        s.update(id=None)
        expected = "[Square] ({}) 9/9 - 9".format(s.id)
        self.assertEqual(expected, str(s))

    def test_update_kwargs_None_id(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None, size=3, x=11)
        expected = "[Square] ({}) 11/10 - 3".format(s.id)
        self.assertEqual(expected, str(s))

    def test_update_kwargs_double(self):
        s = Square(11, 11, 9, 8)
        s.update(id=19, x=1)
        s.update(y=1, x=11, size=3)
        self.assertEqual("[Square] (19) 11/1 - 3", str(s))

    def test_update_kwargs_invalid_size(self):
        s = Square(9, 9, 11, 11)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="num")

    def test_update_kwargs_size_zero(self):
        s = Square(11, 2, 12, 13)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

    def test_update_kwargs_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-3)

    def test_update_kwargs_invalid_x(self):
        s = Square(9, 11, 11, 12)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="num")

    def test_update_kwargs_x_negative(self):
        s = Square(7, 7, 7, 7)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-3)

    def test_update_kwargs_invalid_y(self):
        s = Square(7, 7, 7, 7)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="num")

    def test_update_kwargs_y_negative(self):
        s = Square(7, 7, 7, 7)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-2)


class test_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Square class."""
    def test_square_to_dictionary(self):
        s = Square(1, 2, 3, 4)
        expected_result = {'id': 4, 'size': 1, 'x': 2, 'y': 3}
        self.assertEqual(s.to_dictionary(), expected_result)


if __name__ == "__main__":
    unittest.main()
