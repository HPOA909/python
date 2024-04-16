#Reference https://www.youtube.com/watch?v=ZDa-Z5JzLYM
#Creating and instantiating simple classes
#Employee class
#inside the __init__ method we are going to set all those instance variables
#when we say self is the instance what we mean by that is when we set  self.first=first
#it is the same like saying emp_1.first='Corey'
#except now insted of doing this manually we do it through the __init__method
#it will be done automatically when we create our employee object

#when we create the instance Employee the self argument the instance is passed automatically
#so you can leave it out
#so you need only to pass first, last , and pay values
#you need to pass them in order



class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

 #what will happen when we run the code below __init__method will be called automatically
 #and self (instance)will be passed automatically
 #and it will set all those attributes
 #emp_1.first, emp_1.last, emp_1.email and emp_1.pay

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)