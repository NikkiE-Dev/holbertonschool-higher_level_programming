#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test(self):
        self.assertEqual(max_integer([1, 2, 3, 5]), 5)

    def one_neg_number(self):
        self.assertEqual(max_integer([-2, 0, 2, 4]), 4)

    def all_neg_numbers(self):
        self.assertEqual(max_integer([-4, -6, -8, -2]), 8)

    def max_in_midd(self):
        self.assertEqual(max_integer([4, 6, 8, 2, 0]), 8)

    def list_is_empty(self):
        self.assertIsNone(max_integer([]))

    def one_elem(self):
        self.assertRaises(TypeError, max_integer(2))
