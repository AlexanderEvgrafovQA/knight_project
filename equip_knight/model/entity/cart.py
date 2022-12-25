from equip_knight.model.entity import *

class Cart:
    def __init__(self):
        self._items = []

    def add(self, item):
        if isinstance(item, Item):
            self._items.append(item)

    def get(self, index):
        if isinstance(index, int) and 0 <= index < len(self._items):
            return self._items[index]

    def get_all(self):
        return self._items


    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        if isinstance(index, int) and 0 <= index < len(self):
            return self._items[index]
        else:
            raise Exception()

    def __setitem__(self, index, value):
        if isinstance(index, int) and 0 <= index < len(self) and isinstance(value, Item):
            self._items[index] = value
        else:
            raise Exception()

    def __delitem__(self, index):
        if isinstance(index, int) and 0 <= index < len(self):
            del self._items[index]
        else:
            raise Exception()


    def clear(self):
        self._items = []

    def calculate_total_price(self):
        total = 0
        for i in range(len(self._items)):
            item = self.get(i)
            if isinstance(item, Item):
                total += item.price

        return total

    def __str__(self):
        if not self._items:
            return f"Cart is empty. It`s {len(self._items)} cart slots"
        else:
            msg = "Cart list:\n"
            for item in self._items:
                msg += str(item) + "\n"
        msg += f"There are {len(self._items) - len(self)} empty slots"
        return msg