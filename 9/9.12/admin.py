from user import User


class Admin(User):
    """管理员"""

    def __init__(self, first_name, last_name):
        super(Admin, self).__init__(first_name, last_name)
        self.privileges = Privileges()

    def show_privileges(self):
        print(self.privileges)


class Privileges:
    """权限"""

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(self.privileges)
