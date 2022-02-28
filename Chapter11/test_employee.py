from distutils.command.build_scripts import first_line_re
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        first_name = "John"
        last_name = "Doe"
        annual_salary = 5000
        self.employee = Employee(first_name, last_name, annual_salary)
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 10000)
    def test_give_custom_raise(self):
        amount = 10000
        self.employee.give_raise(amount)
        self.assertEqual(self.employee.annual_salary, 15000)

if __name__ == '__main__':
    unittest.main()