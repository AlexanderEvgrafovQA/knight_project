from equip_knight.model.entity import *

class Shop:
    def __init__(self, items):
        self._items = items
        self.cart = Cart()

    def calculate_total_price_in_cart(self):
        return self.cart.calculate_total_price()
