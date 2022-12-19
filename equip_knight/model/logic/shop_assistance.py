from equip_knight.model.entity import *

class ShopAssistance:

    @staticmethod
    def buy(shop, knight):
        items = shop.cart.get_all()
        knight.inventory.add_items(items)
        knight.remove_coins(shop.cart.calculate_total_price())
        shop.cart.clear()
