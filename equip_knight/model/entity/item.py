class Item:

    def __init__(self, price=0, weight=0):
        self._price = price
        self._weight = weight
        self._slot_type = None

    @property
    def price(self):
        return self._price

    def set_price(self, price):
        if price >= 0:
            self._price = price
        else:
            if not hasattr(self, "_price"):
                self._price = 0
            else:
                raise ValueError("Item price was wrong")

    @price.deleter
    def price(self):
        del self._price

    def get_slot_type(self):
        return self._slot_type

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if weight > 0:
            self._weight = weight
        else:
            raise Exception()

    @weight.deleter
    def weight(self):
        del self._weight

    def __str__(self):
        return (f"price = {self.price}, "
                f"weight = {self._weight}")