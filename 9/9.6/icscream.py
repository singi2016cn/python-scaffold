from restaurant import Restaurant


class IceCreamStand(Restaurant):
    """冰淇淋小店"""

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['bing', 'mangguo', 'li']

    def show_flavors(self):
        print(self.flavors)


ice = IceCreamStand('中餐馆', '粤菜')
ice.describe_restaurant()
ice.show_flavors()
