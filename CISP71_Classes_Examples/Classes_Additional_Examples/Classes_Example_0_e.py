#Reference https://www.youtube.com/watch?v=BJ-VvGyQxho
#Following is the example of a class variable
#class variables are variables that are shared among all instances of the class
#so while instance variables can be unique for each instance names, email pay
#class variables should be the same for each instance
#If you look at our employee class
#what data would we want to be shared among all employees
#let us say that our company gives annual raises every year
#the amount can be changed from year to year but whenever that amount is it's going to be the 
#the same for all employees. So that would be good candidate 
#for a class variable
class Employee:
    
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amt)
        
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000) 

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay) 

print("Employee raise_amt",Employee.raise_amt)   
#print("emp_1.raise_amount", emp_1.raise_amount)
#print(("emp_2.raise_amount", emp_2.raise_amount))

print("Number of employees up to now: ", Employee.num_of_emps)