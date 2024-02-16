#!/usr/bin/python3
"""Defines unittests for models/rectangle.py"""


import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_width(unittest.TestCase):
    """Unittests for testing initialization of Rectangle width attribute."""

    def testnone_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("name", 2)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(3.5, 1)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 2)

    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)


class TestRectangle_height(unittest.TestCase):
    """Unittests for testing initialization of Rectangle height attribute."""

    def test_none_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "num")

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 3.5)

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"a": 1, "b": 2})

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3])

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 2, 3})

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2, 3))

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


class TestRectangle_x(unittest.TestCase):
    """Unittests for testing initialization of Rectangle x attribute."""

    def test_none_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 1, "b": 2}, 2)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True, 2)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3), 2)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(4, 2, -2, 0)


class TestRectangle_y(unittest.TestCase):
    """Unittests for testing initialization of Rectangle y attribute."""

    def test_none_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 2.5)

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)


class TestRectangleArea(unittest.TestCase):
    """unittest for area calculation"""

    def test_area_with_positive_dimensions(self):
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

    def test_area_one_arg(self):
        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)


class TestRectangle_stdout_display(unittest.TestCase):
    """Unittests for testing  display methods of Rectangle class."""

    @staticmethod
    def get_stdout(rect, method):
        """Gets and returns text printed to stdout.

        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        pick = io.StringIO()
        sys.stdout = pick
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return pick

    def test_str_method_print_width_height(self):
        r = Rectangle(3, 6)
        pick = TestRectangle_stdout_display.get_stdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 3/6\n".format(r.id)
        self.assertEqual(correct, pick.getvalue())

    def test_str_method_width_height_x(self):
        r = Rectangle(5, 5, 1)
        output = "[Rectangle] ({}) 1/0 - 5/5".format(r.id)
        self.assertEqual(output, r.__str__())

    def test_str_method_width_height_x_y(self):
        r = Rectangle(2, 9, 3, 5)
        correct = "[Rectangle] ({}) 3/5 - 2/9".format(r.id)
        self.assertEqual(correct, str(r))

    def test_str_method_one_arg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

    # Test display method
    def test_display_width_height(self):
        r = Rectangle(2, 3, 0, 0, 0)
        pick = TestRectangle_stdout_display.get_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", pick.getvalue())

    def test_display_width_height_x(self):
        r = Rectangle(3, 2, 1, 0, 1)
        pick = TestRectangle_stdout_display.get_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", pick.getvalue())

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
