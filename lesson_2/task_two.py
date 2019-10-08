class Shop:
    QUANTITY_OF_GOODS = 0
    
    def set_shop_name(self, value):
        self._shop_name = value

    def get_shop_name(self):
        return self._shop_name

    def set_quantity_of_goods(self, value):
        self._quantity_of_goods += value

    def get_quantity_of_goods(self):
        return self._quantity_of_goods


class MyShop(Shop):

    def __init__(self, shop_name, quantity_of_goods):
        self._shop_name = shop_name
        self._quantity_of_goods = quantity_of_goods


shop = MyShop('Silpo', 20000)

print(shop.get_shop_name())
print(shop.get_quantity_of_goods())
