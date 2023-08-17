#!/usr/bin/env python3

import unittest
from ingredient import Ingredient
from item import Item
from product import Product

class TestItem(unittest.TestCase):
    def test_can_be_an_ingredient(self):
        i = Item("foo")
        self.assertTrue(isinstance(i, Ingredient))

    def test_can_be_a_product(self):
        i = Item("foo")
        self.assertTrue(isinstance(i, Product))
        
    def test_repr(self):
        i = Item("foo")
        s = i.__repr__()
        i2 = eval(s)
        self.assertEqual(i, i2)

    def test_equal(self):
        i = Item("foo")
        i2 = Item("foo")
        self.assertTrue(i == i)
        self.assertTrue(i == i2)

    def test_notequal(self):
        i = Item("foo")
        i2 = Item("bar")
        self.assertTrue(i != i2)
        self.assertFalse(i == i2)

    def test_is_hashable(self):
        i = Item("foo")
        d = { i : 1 }

if __name__ == '__main__':
    unittest.main()
