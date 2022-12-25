from equip_knight.model.entity import  *

class Sorter:
    @staticmethod
    def sort(cart):
        if isinstance(cart, Cart):
            for i in range(len(cart) -1):
                for index in range(len(cart) -1 -i):
                    if cart[index].price > cart[index+1].price:
                        temp = cart[index]
                        cart[index] = cart[index + 1]
                        cart[index + 1] = temp
