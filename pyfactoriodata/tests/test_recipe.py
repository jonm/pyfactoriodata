#!/usr/bin/env python3

import unittest
from item import Item
from recipe import Recipe
from technology import Technology

class TestRecipe(unittest.TestCase):

    def _make_recipe(self,
                     name = "a-recipe",
                     results = { Item("item1",100) : 1 },
                     ingredients = { Item("item2",100) : 2 },
                     crafting_time_secs = 1.0,
                     crafted_only_in = Item("item3",100),
                     enabled_by = Technology("tech1", 1, 1, {}),
                     expensive_version = Recipe(
                         name = "a-recipe",
                         results = { Item("item1",100) : 1 },
                         ingredients = { Item("item2",100) : 4 },
                         crafting_time_secs = 2.0,
                         crafted_only_in = Item("item3",100),
                         enabled_by = Technology("tech1", 1, 1, {}))):
        return Recipe(
            name = name,
            results = results,
            ingredients = ingredients,
            crafting_time_secs = crafting_time_secs,
            crafted_only_in = crafted_only_in,
            enabled_by = enabled_by,
            expensive_version = expensive_version)
    
    def test_repr(self):
        r = self._make_recipe()
        s = r.__repr__()
        r2 = eval(s)
        self.assertEqual(r, r2)

    def test_equal(self):
        r = self._make_recipe()
        r2 = self._make_recipe()
        self.assertTrue(r == r)
        self.assertTrue(r == r2)

    def test_notequal_name(self):
        r = self._make_recipe(name = "foo")
        r2 = self._make_recipe(name = "bar")
        self.assertTrue(r != r2)
        self.assertFalse(r == r2)

    def test_notequal_results(self):
        r = self._make_recipe(results = { Item("foo",100) : 1 })
        r2 = self._make_recipe(results = { Item("foo",100) : 3 })
        r3 = self._make_recipe(results = { Item("bar",100) : 1 })
        self.assertTrue(r != r2)
        self.assertFalse(r == r2)
        self.assertTrue(r != r3)
        self.assertFalse(r == r3)
        self.assertTrue(r2 != r3)
        self.assertFalse(r2 == r3)

    def test_notequal_ingredients(self):
        r = self._make_recipe(ingredients = { Item("foo",100) : 1 })
        r2 = self._make_recipe(ingredients = { Item("foo",100) : 3 })
        r3 = self._make_recipe(ingredients = { Item("bar",100) : 1 })
        self.assertTrue(r != r2)
        self.assertFalse(r == r2)
        self.assertTrue(r != r3)
        self.assertFalse(r == r3)
        self.assertTrue(r2 != r3)
        self.assertFalse(r2 == r3)

    def test_notequal_crafting_time_secs(self):
        r = self._make_recipe(crafting_time_secs = 1.0)
        r2 = self._make_recipe(crafting_time_secs = 2.0)
        self.assertTrue(r != r2)
        self.assertFalse(r == r2)

    def test_notequal_crafted_only_in(self):
        r = self._make_recipe(crafted_only_in = None)
        r2 = self._make_recipe(crafted_only_in = Item("foo",100))
        r3 = self._make_recipe(crafted_only_in = Item("bar",100))
        self.assertTrue(r != r2)
        self.assertFalse(r == r2)
        self.assertTrue(r != r3)
        self.assertFalse(r == r3)
        self.assertTrue(r2 != r3)
        self.assertFalse(r2 == r3)

    def test_notequal_enabled_by(self):
        r = self._make_recipe(enabled_by = None)
        r2 = self._make_recipe(enabled_by = Technology("foo",1,2,{},[]))
        r3 = self._make_recipe(enabled_by = Technology("bar",1,2,{},[]))
        self.assertTrue(r != r2)
        self.assertFalse(r == r2)
        self.assertTrue(r != r3)
        self.assertFalse(r == r3)
        self.assertTrue(r2 != r3)
        self.assertFalse(r2 == r3)

    def test_notequal_expensive_version(self):
        r = self._make_recipe(expensive_version = None)
        r2 = self._make_recipe(expensive_version = self._make_recipe(name = "foo"))
        r3 = self._make_recipe(expensive_version = self._make_recipe(name = "bar"))
        self.assertTrue(r != r2)
        self.assertFalse(r == r2)
        self.assertTrue(r != r3)
        self.assertFalse(r == r3)
        self.assertTrue(r2 != r3)
        self.assertFalse(r2 == r3)
        
    def test_is_hashable(self):
        r = self._make_recipe()
        d = { r : 1 }

if __name__ == '__main__':
    unittest.main()
