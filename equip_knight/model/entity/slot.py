class Slot():
    def __init__(self, type, item=None):
        self._type = type
        self._item = item

    def get_slot_type(self):
        return self._type

    def set_item(self, item):
        self._item = item

    def get_item(self):
        return self._item