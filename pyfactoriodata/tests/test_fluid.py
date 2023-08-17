#!/usr/bin/env python3

import unittest
from ingredient import Ingredient
from fluid import Fluid
from product import Product

class TestFluid(unittest.TestCase):
    def test_can_be_an_ingredient(self):
        f = Fluid("foo",15,0.1)
        self.assertTrue(isinstance(f, Ingredient))

    def test_can_be_a_product(self):
        f = Fluid("foo",15,0.1)
        self.assertTrue(isinstance(f, Product))
        
    def test_repr(self):
        f = Fluid("foo",15,0.1)
        s = f.__repr__()
        f2 = eval(s)
        self.assertEqual(f, f2)

    def test_equal(self):
        f = Fluid("foo",15,0.1)
        f2 = Fluid("foo",15,0.1)
        self.assertTrue(f == f)
        self.assertTrue(f == f2)

    def test_notequal_name(self):
        f = Fluid("foo",15,0.1)
        f2 = Fluid("bar",15,0.1)
        self.assertTrue(f != f2)
        self.assertFalse(f == f2)

    def test_notequal_default_temperature(self):
        f = Fluid("foo",15,0.1)
        f2 = Fluid("foo",777,0.1)
        self.assertTrue(f != f2)
        self.assertFalse(f == f2)

    def test_notequal_heat_capacity(self):
        f = Fluid("foo",15,0.1)
        f2 = Fluid("foo",15,0.333)
        self.assertTrue(f != f2)
        self.assertFalse(f == f2)

    def test_notequal_max_temperature(self):
        f = Fluid("foo",15,0.1,max_temperature=5)
        f2 = Fluid("foo",15,0.333)
        f3 = Fluid("foo",15,0.1,max_temperature=10)
        self.assertTrue(f != f2)
        self.assertFalse(f == f2)
        self.assertTrue(f != f3)
        self.assertFalse(f == f3)
        self.assertTrue(f2 != f3)
        self.assertFalse(f2 == f3)
        
    def test_notequal_gas_temperature(self):
        f = Fluid("foo",15,0.1,gas_temperature=2)
        f2 = Fluid("foo",15,0.1,gas_temperature=888)
        f3 = Fluid("foo",15,0.1)
        self.assertTrue(f != f2)
        self.assertFalse(f == f2)
        self.assertTrue(f != f3)
        self.assertFalse(f == f3)
        self.assertTrue(f2 != f3)
        self.assertFalse(f2 == f3)
        
    def test_is_hashable(self):
        f = Fluid("foo",15,0.1,max_temperature=3,gas_temperature=4)
        d = { f : 1 }

if __name__ == '__main__':
    unittest.main()
