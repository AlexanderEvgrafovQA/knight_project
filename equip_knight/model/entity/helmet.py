from equip_knight.model.entity import *

class Helmet(Item):
    def __init__(self, price, weight, armor):
        super().__init__(price, weight)
        self._armor = armor
        self._slot_type = "head"

