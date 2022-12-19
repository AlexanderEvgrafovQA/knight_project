from equip_knight.model.entity import *

class ChectArmor(Item):
    def __init__(self, price, weight, armor):
        super().__init__(price, weight)
        self._armor = armor
