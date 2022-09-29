import requests

class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'

#emp_1 = Employee('Corey', 'Schafer', 50000)
#emp_2 = Employee('Sue', 'Smith', 60000)

#print(emp_1.pay, str(int(50000 * Employee.raise_amt)))
#print(emp_2.pay,  str(int(60000 * Employee.raise_amt)))