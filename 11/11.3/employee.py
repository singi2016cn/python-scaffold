"""雇员"""


class Employee:
    """雇员"""

    def __init__(self, first_name, last_name, yearly_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.yearly_salary = yearly_salary

    def give_raise(self):
        self.yearly_salary += 5000
