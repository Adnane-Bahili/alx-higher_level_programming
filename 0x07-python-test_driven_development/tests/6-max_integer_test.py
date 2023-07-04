#!/usr/bin/python3
"""Unittests for max_integer([..])."""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """defines unittests for max_integer([..])"""
    def test_ordered_list(self):
        """testing an ordered list of integers"""
        ordered = [7, 25, 49, 67]
        self.assertEqual(max_integer(ordered), 67)

    def test_unordered_list(self):
        """testing an unordered list of integers"""
        unordered = [32, 86, 74, 21]
        self.assertEqual(max_integer(unordered), 86)

    def test_max_at_begginning(self):
        """testing a list with a beginning max value"""
        max_at_beginning = [65, 25, 20, 8]
        self.assertEqual(max_integer(max_at_beginning), 65)

    def test_empty_list(self):
        """testing an empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """testing a list with a single element"""
        one_element = [56]
        self.assertEqual(max_integer(one_element), 56)

    def test_floats(self):
        """testing a list of floats"""
        floats = [94.5, 35.26, 23.4, 75.12, 49.12]
        self.assertEqual(max_integer(floats), 94.5)

    def test_ints_and_floats(self):
        """testing a list of ints and floats"""
        ints_and_floats = [5.65, 68.2, 89, 23, 14]
        self.assertEqual(max_integer(ints_and_floats), 89)

    def test_string(self):
        """testing a string"""
        string = "Jack"
        self.assertEqual(max_integer(string), 'k')

    def test_list_of_strings(self):
        """testing a list of strings"""
        strings = ["Julie", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """testing an empty string"""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
