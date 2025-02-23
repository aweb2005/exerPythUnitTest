import unittest
from employee import Employee
from unittest.mock import patch
# make it all "DRY" = don't repeat yourself
# all test should be stand-alone. not dependent on any other tests.

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls): #now you can setup and teardown something before and after all the tests, not each test
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self) -> None: #don't have to create test employees in each test case now, just once
        print('setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self) -> None:
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        #emp_1 = Employee('Corey', 'Schafer', 50000)
        #emp_2 = Employee('Sue', 'Smith', 60000)

        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        print('test_fullname')
        #emp_1 = Employee('Corey', 'Schafer', 50000)
        #emp_2 = Employee('Sue', 'Smith', 60000)

        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        print('test_apply_raise')
        #emp_1 = Employee('Corey', 'Schafer', 50000)
        #emp_2 = Employee('Sue', 'Smith', 60000)

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

#        self.assertEqual(self.emp_1.pay, '52500')
#        self.assertEqual(self.emp_2.pay, '63000')
        self.assertEqual(self.emp_1.pay, int(50000 * Employee.raise_amt))
        self.assertEqual(self.emp_2.pay,  int(60000 * Employee.raise_amt))

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')

if __name__ == '__main__':
    unittest.main()