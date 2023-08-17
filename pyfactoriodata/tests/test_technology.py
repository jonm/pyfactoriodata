#!/usr/bin/env python3

import unittest
from technology import Technology
from item import Item

class TestTechnology(unittest.TestCase):
    def test_repr(self):
        t = Technology("foo",1,2,{},[])
        s = t.__repr__()
        t2 = eval(s)
        self.assertEqual(t, t2)

    def test_requires_with_no_prereqs(self):
        t = Technology("foo",1,2,{},[])
        t2 = Technology("bar",3,4,{},[])
        self.assertFalse(t.requires(t2))

    def test_requires_direct_prereq(self):
        t = Technology("foo",1,2,{},[])
        t2 = Technology("bar",3,4,{},[t])
        self.assertTrue(t2.requires(t))
        self.assertFalse(t.requires(t2))

    def test_requires_transitive_prereq(self):
        t = Technology("foo",1,2,{},[])
        t2 = Technology("bar",3,4,{},[t])
        t3 = Technology("baz",5,6,{},[t2])
        self.assertTrue(t3.requires(t))
        self.assertFalse(t.requires(t3))

    def test_equal(self):
        t = Technology("foo",1,2,{},[])
        t2 = Technology("foo",1,2,{},[])
        self.assertTrue(t == t)
        self.assertTrue(t == t2)

    def test_notequal_name(self):
        t = Technology("foo",1,2,{},[])
        t2 = Technology("bar",1,2,{},[])
        self.assertTrue(t != t2)
        self.assertFalse(t == t2)

    def test_notequal_cost_count(self):
        t = Technology("foo",1,2,{},[])
        t2 = Technology("foo",777,2,{},[])
        self.assertTrue(t != t2)
        self.assertFalse(t == t2)
        
    def test_notequal_cycle_time_secs(self):
        t = Technology("foo",1,2,{},[])
        t2 = Technology("foo",1,888,{},[])
        self.assertTrue(t != t2)
        self.assertFalse(t == t2)

    def test_notequal_ingredients(self):
        t = Technology("foo",1,2,{},[])
        t2 = Technology("foo",1,2,{Item("item",100) : 1},[])
        self.assertTrue(t != t2)
        self.assertFalse(t == t2)

    def test_notequal_prereqs(self):
        t = Technology("foo",1,2,{},[])
        t3 = Technology("bar",3,4,{},[])
        t2 = Technology("foo",1,2,{},[t3])
        self.assertTrue(t != t2)
        self.assertFalse(t == t2)

    def test_lt_checks_types(self):
        t = Technology("foo",1,2,{},[])
        with self.assertRaises(TypeError):
            t < 1

    def test_lt_noncomparable(self):
        t = Technology("foo",1,2,{},[])
        t2 = Technology("bar",3,4,{},[])
        self.assertFalse(t < t2)
        self.assertFalse(t2 < t)
        self.assertFalse(t < t)

    def test_lt_with_prereqs(self):
        t = Technology("foo",1,2,{},[])
        t2 = Technology("bar",3,4,{},[t])
        self.assertTrue(t < t2)
        self.assertFalse(t2 < t)

    def test_le_checks_types(self):
        t = Technology("foo",1,2,{},[])
        with self.assertRaises(TypeError):
            t <= 1

    def test_le_noncomparable(self):
        t = Technology("foo",1,2,{},[])
        t2 = Technology("bar",3,4,{},[])
        self.assertFalse(t <= t2)
        self.assertFalse(t2 <= t)

    def test_le_with_prereqs(self):
        t = Technology("foo",1,2,{},[])
        t2 = Technology("bar",3,4,{},[t])
        self.assertTrue(t <= t2)
        self.assertFalse(t2 <= t)

    def test_le_with_equality(self):
        t = Technology("foo",1,2,{},[])
        t2 = Technology("foo",1,2,{},[])
        self.assertTrue(t <= t2)
        self.assertTrue(t2 <= t)
        self.assertTrue(t <= t)

    def test_gt_checks_types(self):
        t = Technology("foo",1,2,{},[])
        with self.assertRaises(TypeError):
            t > 1

    def test_gt_noncomparable(self):
        t = Technology("foo",1,2,{},[])
        t2 = Technology("bar",3,4,{},[])
        self.assertFalse(t > t2)
        self.assertFalse(t2 > t)
        self.assertFalse(t > t)

    def test_gt_with_prereqs(self):
        t = Technology("foo",1,2,{},[])
        t2 = Technology("bar",3,4,{},[t])
        self.assertFalse(t > t2)
        self.assertTrue(t2 > t)

    def test_ge_checks_types(self):
        t = Technology("foo",1,2,{},[])
        with self.assertRaises(TypeError):
            t >= 1

    def test_ge_noncomparable(self):
        t = Technology("foo",1,2,{},[])
        t2 = Technology("bar",3,4,{},[])
        self.assertFalse(t >= t2)
        self.assertFalse(t2 >= t)

    def test_ge_with_prereqs(self):
        t = Technology("foo",1,2,{},[])
        t2 = Technology("bar",3,4,{},[t])
        self.assertFalse(t >= t2)
        self.assertTrue(t2 >= t)

    def test_ge_with_equality(self):
        t = Technology("foo",1,2,{},[])
        t2 = Technology("foo",1,2,{},[])
        self.assertTrue(t >= t2)
        self.assertTrue(t2 >= t)
        self.assertTrue(t >= t)

    def test_is_hashable(self):
        t = Technology("foo",1,2,{},[])
        d = { t : 1 }

if __name__ == '__main__':
    unittest.main()
