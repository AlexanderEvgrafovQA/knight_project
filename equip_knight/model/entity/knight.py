from equip_knight.model.entity import *

class Knight:
    def __init__(self, coins):
        self._coins = coins
        self.inventory = Inventory()
        self.head_slot = Slot("head")
        self.chest_slot = Slot("chest")
        self.right_hand_slot = Slot("right hand")
        self.left_hand_slot = Slot("left hand")

    def remove_coins(self, price):
        self._coins = self._coins - price

    def equip(self, item):
        if self.head_slot.get_slot_type() == item.get_slot_type():
            self.head_slot.set_item(item)


