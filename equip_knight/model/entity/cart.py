from equip_knight.model.entity import *

class Cart:
    def __init__(self):
        self._items = []

    def add(self, item):
        if isinstance(item, Item):
            self._items.append(item)

    def get(self, index):
        if isinstance(index, int) and 0 <= index < self.size():
            return self._items[index]

    def get_all(self):
        return self._items

    def size(self):
        return len(self._items)

    def __str__(self):
        return f""

    def clear(self):
        self._items = []

    def calculate_total_price(self):
        total = 0
        for i in range(self.size()):
            item = self.get(i)
            if isinstance(item, Item):
                total += item.price

        return total