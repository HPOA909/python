#Reference https://www.youtube.com/watch?v=ZDa-Z5JzLYM
#Creating and instantiating simple classes
#Employee class
#let us add an action let us say we want to add the ability to display the full name


class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)