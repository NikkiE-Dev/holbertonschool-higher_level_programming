#!/usr/bin/python3
"""Unittest for Base"""
import unittest
from models.base import Base


class TestBase(unitest.TestCase):

    def test(self):
        self.assertEqual(Base(), 1)
