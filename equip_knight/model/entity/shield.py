from equip_knight.model.entity import *

class Shield(Item):
    def __init__(self, price, weight, block_damage=0):
        super().__init__(price, weight)
        self._block_damage = block_damage
        self._slot_type = "left hand"

    def get_slot_type(self):
        return self._slot_type

    @property
    def block(self):
        return self._block_damage

    @block.setter
    def block(self, block_damage):
        if block_damage > 0:
            self._block_damage = block_damage
        else:
            raise Exception()

    @block.deleter
    def block(self):
        del self._block_damage