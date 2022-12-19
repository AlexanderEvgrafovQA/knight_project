import unittest
from equip_knight.model.entity import *
from equip_knight.model.logic import *


class TestShopAssistance(unittest.TestCase):
    def test_buy(self):
        helmet = Helmet(10, 20, 30)
        sword = Sword(12, 25, 9)
        items = [helmet, sword]
        shop = Shop(items)
        knight = Knight(500)
        ShopAssistance.buy(shop, knight)

        expected = 500-22

        actual = knight._coins

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()