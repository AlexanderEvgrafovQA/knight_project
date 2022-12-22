from equip_knight.model.entity import *

class Sword(Item):
    def __init__(self, price, weight, damage):
        super().__init__(price, weight)
        self._damage = damage
        self._slot_type = "right hand"

    def get_slot_type(self):
        return self._slot_type

