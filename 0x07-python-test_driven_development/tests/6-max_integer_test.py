#!/usr/bin/python3

"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_sorted_list(self):
        """Test an sorted list of integers."""
        sorted = [3, 4, 6]
        self.assertEqual(max_integer(sorted), 6)

    def test_unsorted_list(self):
        """Test an unsorted list of integers."""
        unsorted = [3, 1, 6]
        self.assertEqual(max_integer(unsorted), 6)

    def test_negative_list(self):
        """Test an negative list of integers."""
        negative = [-3, -4, -6]
        self.assertEqual(max_integer(negative), -3)

    def test_string(self):
        """Test with string."""
        string = "Men"
        self.assertEqual(max_integer(string), 'n')

    def test_float(self):
        """Test list of floats."""
        floats = [3.9, 4.9, 0.6]
        self.assertEqual(max_integer(floats), 4.9)


if __name__ == "__main__":
    unittest.main()
