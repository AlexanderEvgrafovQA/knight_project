import unittest
from equip_knight.model.entity import *
from equip_knight.model.logic import *


class TestEquip(unittest.TestCase):
    def test_equip(self):
        knight = Knight(500)
        item = Helmet(10, 20, 30)
        knight.equip(item)

        expected = item

        actual = knight.head_slot.get_item()

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()