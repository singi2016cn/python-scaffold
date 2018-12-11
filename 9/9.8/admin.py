from privileges import Privileges


class Admin:
    """管理员"""

    def __init__(self):
        self.privileges = Privileges()


admin = Admin()
admin.privileges.show_privileges()
