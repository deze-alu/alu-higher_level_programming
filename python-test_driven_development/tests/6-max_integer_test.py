#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Checks the behaviour of the max_integer function."""

    def test_ordered_list(self):
        """The biggest value sits at the end of the list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """The biggest value sits in the middle of the list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_biggest_first(self):
        """The biggest value sits at the beginning of the list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_one_element(self):
        """A single element is the biggest one."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """An empty list holds no maximum."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """The argument defaults to an empty list."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """The maximum of negative values is the closest one to zero."""
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_mixed_signs(self):
        """Positive and negative values are compared together."""
        self.assertEqual(max_integer([-10, 5, -3, 2]), 5)

    def test_repeated_maximum(self):
        """A maximum appearing twice is returned once."""
        self.assertEqual(max_integer([4, 4, 2]), 4)

    def test_all_equal(self):
        """Every value being equal, that value is the maximum."""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_floats(self):
        """Floats compare like any other number."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_mixed_numbers(self):
        """Integers and floats can be mixed."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_strings(self):
        """Strings are ordered alphabetically."""
        self.assertEqual(max_integer(["ab", "zz", "cd"]), "zz")

    def test_single_string(self):
        """A string is a list of characters."""
        self.assertEqual(max_integer("hello"), "o")

    def test_zero(self):
        """Zero is returned when it is the only value."""
        self.assertEqual(max_integer([0]), 0)

    def test_not_a_list(self):
        """An integer holds no length."""
        with self.assertRaises(TypeError):
            max_integer(7)

    def test_uncomparable_types(self):
        """A string cannot be compared with an integer."""
        with self.assertRaises(TypeError):
            max_integer([1, "two"])


if __name__ == '__main__':
    unittest.main()
