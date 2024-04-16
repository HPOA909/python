#9.3.1: Adding methods to a class
class Employee:
    def __init__(self):
        self.wage = 0
        self.hours_worked = 0

#   def ... Add new method here ...
#        ...

alice = Employee()
alice.wage = 9.25
alice.hours_worked = 35
print('Alice:\n Net pay: {:.2f}'.format(alice.calculate_pay()))

barbara = Employee()
barbara.wage = 11.50
barbara.hours_worked = 20
print('Barbara:\n Net pay: {:.2f}'.format(barbara.calculate_pay()))
