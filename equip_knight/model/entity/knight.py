from equip_knight.model.entity import *

class Knight:
    def __init__(self, coins):
        self._coins = coins
        self.inventory = Inventory()

    def remove_coins(self, price):
        self._coins = self._coins - price
