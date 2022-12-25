import unittest

from equip_knight.model.entity import *
from equip_knight.model.logic import *


class TestCart(unittest.TestCase):

    def test_calculate_total_price_basic(self):
        cart = Cart()
        cart.add(Item(1.5))
        cart.add(Item(2.5))
        cart.add(Item(3.5))
        expected = 7.5

        actual = Cart.calculate_total_price(cart)

        self.assertEqual(expected, actual)

    def test_calculate_total_price_with_incorrect_data(self):
        expected = -1
        actual = Cart.calculate_total_price(10)

        self.assertEqual(expected, actual)

    def test_calculate_total_price_with_empty_cart(self):
        expected = 0
        actual = Cart.calculate_total_price(Cart())

        self.assertEqual(expected, actual)

    def test_calculate_total_price_with_only_one_product(self):
        cart = Cart()
        item = Item(10)
        cart.add(item)
        expected = item.price

        actual = Cart.calculate_total_price(cart)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()