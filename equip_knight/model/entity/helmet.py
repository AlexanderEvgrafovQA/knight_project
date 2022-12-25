from equip_knight.model.entity import *

class Helmet(Item):
    def __init__(self, price, weight, armor=0):
        super().__init__(price, weight)
        self._armor = armor
        self._slot_type = "head"

    @property
    def armor(self):
        return self._armor

    @armor.setter
    def armor(self, armor):
        if armor > 0:
            self._armor = armor
        else:
            raise Exception()

    @armor.deleter
    def armor(self):
        del self._armor


