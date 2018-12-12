from user import User
from privileges import Privileges


class Admin(User):
    """管理员"""

    def __init__(self, first_name, last_name):
        super(Admin, self).__init__(first_name, last_name)
        self.privileges = Privileges()

    def show_privileges(self):
        print(self.privileges)
