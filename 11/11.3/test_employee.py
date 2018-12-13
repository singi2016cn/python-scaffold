import unittest

from employee import Employee


class EmployeeTestCase(unittest.TestCase):
    """雇员的测试用例"""

    def setUp(self):
        self.employee = Employee('sin', 'gi', 100000)

    def test_give_default_raise(self):
        """测试原有的年薪"""
        self.assertEqual(self.employee.yearly_salary, 100000)

    def test_give_custom_raise(self):
        """测试加薪后的年薪"""
        self.employee.give_raise()
        self.assertEqual(self.employee.yearly_salary, 105000)


if __name__ == '__main__':
    unittest.main()
