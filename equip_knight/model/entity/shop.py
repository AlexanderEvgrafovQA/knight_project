from equip_knight.model.entity import *

class Shop:
    def __init__(self, items):
        self._items = items
        self.cart = Cart()
