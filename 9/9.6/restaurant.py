class Restaurant:
    """就餐人数"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant)
        print(self.cuisine_type)

    def open_restaurant(self):
        print('正在营业')

    def increment_number_served(self, number_served):
        self.number_served += number_served

    def set_number_served(self, number_served):
        self.number_served = number_served



