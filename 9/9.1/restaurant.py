class Restaurant:
    """餐馆"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('餐馆名称:' + self.restaurant_name)
        print('餐品名称:' + self.cuisine_type)

    def open_restaurant(self):
        print('正在营业')


res = Restaurant('中餐馆', '粤菜')
print(res.restaurant_name)
print(res.cuisine_type)

print(res.describe_restaurant())
