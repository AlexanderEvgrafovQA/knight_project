import unittest
from equip_knight.model.entity import *


class TestItem(unittest.TestCase):
    def test_setter(self):
        item = Item()
        item._price = 10

        expected = 10

        actual = item._price

        self.assertEqual(expected, actual)

    def test_setter_without_price(self):
        item = Item()

        expected = 0

        actual = item._price

        self.assertEqual(expected, actual)

    def test_setter_negative(self):
        item = Item()

        self.assertRaises(ValueError, item.set_price, -10)



if __name__ == "__main__":
    unittest.main()