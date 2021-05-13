#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test(self):
        self.assertEqual(max_integer([1, 2, 3, 5]), 5)

    def test_one_neg_number(self):
        self.assertEqual(max_integer([-2, 0, 2, 4]), 4)

    def test_all_neg_numbers(self):
        self.assertEqual(max_integer([-4, -6, -8, -2]), -2)

    def test_max_in_midd(self):
        self.assertEqual(max_integer([4, 6, 8, 2, 0]), 8)

    def test_list_is_empty(self):
        self.assertIsNone(max_integer([]))

    def test_one_elem(self):
        self.assertEqual(max_integer([2]), 2)

    def test_max_in_beg(self):
        self.assertEqual(max_integer([10, 9, 8, 7]), 10)
