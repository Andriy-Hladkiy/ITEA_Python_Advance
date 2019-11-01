class Shop:
    QUANTITY_OF_GOODS = 0

    def set_shop_name(self, value):
        self._shop_name = value

    def get_shop_name(self):
        return self._shop_name

    def set_quantity_of_goods(self, value):
        self._QUANTITY_OF_GOODS += value

    def get_quantity_of_goods(self):
        return self._QUANTITY_OF_GOODS


class MyShop(Shop):

    def __init__(self, shop_name, QUANTITY_OF_GOODS):
        self._shop_name = shop_name
        self._QUANTITY_OF_GOODS = QUANTITY_OF_GOODS


shop = MyShop('Silpo', 20000)

print(shop.get_shop_name())
print(shop.get_quantity_of_goods())
