class Inventory:
    def __init__(self):
        self._items = []

    def add_items(self, items):
        self._items = self._items + items
