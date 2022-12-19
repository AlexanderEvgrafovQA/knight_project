class Item:

    def __init__(self, price=0, weight=0):
        self.price = price
        self._weight = weight

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price >= 0:
            self._price = price
        else:
            if not hasattr(self, "_price"):
                self._price = 0
            else:
                raise ValueError("Item price was wrong")

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


    def __str__(self):
        return f"price = {self.price}"