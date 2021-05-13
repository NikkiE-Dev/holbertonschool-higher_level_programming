#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    

    def test(self):
        self.assertEqual(max_integer([1, 2, 3, 5]), 5)
        self.assertEqual(max_integer([-2, 0, 2, 4]), 4)
        self.assertRaises(TypeError, max_integer((1, 2)))
        self.assertEqual(max_integer([8, 6, 4, 2]), 8)
        self.assertRaises(TypeError, max_integer((1.14, 2.24)))
        self.assertRaises(TypeError, max_integer(()))
