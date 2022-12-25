from equip_knight.model.entity import *

class Sword(Item):
    def __init__(self, price, weight, damage):
        super().__init__(price, weight)
        self._damage = damage
        self._slot_type = "right hand"

    def get_slot_type(self):
        return self._slot_type

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, damage):
        if damage > 0:
            self._damage = damage
        else:
            raise Exception()

    @damage.deleter
    def damage(self):
        del self._damage
