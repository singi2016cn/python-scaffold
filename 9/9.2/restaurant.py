class Restaurant:
    """三家餐馆"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant)
        print(self.cuisine_type)

    def open_restaurant(self):
        print('正在营业')


res = Restaurant('中餐馆', '粤菜')
res.open_restaurant()

res2 = Restaurant('中餐馆', '粤菜')
res2.open_restaurant()

res3 = Restaurant('中餐馆', '粤菜')
res3.open_restaurant()
