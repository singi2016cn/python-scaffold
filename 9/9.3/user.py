class User:
    """用户"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(self.first_name)
        print(self.last_name)

    def great_user(self):
        print('欢迎'+self.first_name+' '+self.last_name)


user = User('sin', 'gi')
user.describe_user()
user.great_user()
