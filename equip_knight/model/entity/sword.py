from equip_knight.model.entity import *

class Sword(Item):
    def __init__(self, price, weight, damage):
        super().__init__(price, weight)
        self._damage = damage

