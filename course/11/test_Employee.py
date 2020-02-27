import unittest
from Employee import Employee

class EmployeeTestCase(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('Yushun','Xu',10000)
    
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary,15000)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.salary,20000)
        
unittest.main()
