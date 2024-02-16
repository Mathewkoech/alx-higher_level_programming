#!/usr/bin/python3
"""Defines unittests for models/square.py"""

import sys
import unittest
from models.base import Base
from models.square import Square
import io


class TestSquare_size(unittest.TestCase):
    """Unittests for testing size initialization of the Square class."""

    def test_bool_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 1, 4)

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 6, 7])

    def test_none_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(3.4)

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2}, 2)

    def test_range_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(5))

    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)


class TestSquare_x(unittest.TestCase):
    """Unittests for testing initialization of Square x attribute."""

    def test_none_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "num")

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 8.5)

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"a": 1, "b": 2}, 2)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3])

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {1, 2, 3})

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, (1, 5, 7))

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(8, -5, 0)


class TestSquare_y(unittest.TestCase):
    """Unittests for testing initialization of Square y attribute."""

    def test_none_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, "num")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 5, 7.5)

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {"a": 2, "b": 3})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, [1, 2, 2])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, {1, 5, 6})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, (1, 5, 4))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(2, 0, -2)


class TestSquare_stdout(unittest.TestCase):
    """Unittests for testing  display methods of Square class."""

    @staticmethod
    def get_stdout(sq, method):
        """picks and returns text printed to stdout.

        Args:
            sq (Square): The Square ot print to stdout.
            method (str): The method to run on sq.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        pick = io.StringIO()
        sys.stdout = pick
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return pick

    def test_str_method_print_size(self):
        s = Square(3)
        pick = TestSquare_stdout.get_stdout(s, "print")
        output = "[Square] ({}) 0/0 - 3\n".format(s.id)
        self.assertEqual(output, pick.getvalue())

    def test_str_method_size_x(self):
        s = Square(3, 3)
        output = "[Square] ({}) 3/0 - 3".format(s.id)
        self.assertEqual(output, s.__str__())

    def test_str_method_size_x_y(self):
        s = Square(5, 6, 20)
        output = "[Square] ({}) 6/20 - 5".format(s.id)
        self.assertEqual(output, str(s))

    def test_str_method_one_arg(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.__str__(1)

    # Test display method
    def test_display_size(self):
        s = Square(2, 0, 0, 9)
        pick = TestSquare_stdout.get_stdout(s, "display")
        self.assertEqual("##\n##\n", pick.getvalue())

    def test_display_size_x(self):
        s = Square(3, 1, 0, 18)
        pick = TestSquare_stdout.get_stdout(s, "display")
        self.assertEqual(" ###\n ###\n ###\n", pick.getvalue())


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
