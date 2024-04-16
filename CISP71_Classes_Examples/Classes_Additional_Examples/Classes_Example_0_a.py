#Reference https://www.youtube.com/watch?v=ZDa-Z5JzLYM

class Employee:
    pass
emp_1=Employee()
emp_2=Employee()

print(emp_1)
print(emp_2)

emp_1.first='Corey'
emp_1.last='Schafer'
emp_1.email='CShafer@yahoo.com'
emp_1.pay=50000

emp_2.first='Sam'
emp_2.last='Henry'
emp_2.email='SHenry@yahoo.com'
emp_2.pay=60000

#each of those instances have attributes that are unique to them

#instead of setting the attributes manually each time
#We do not get much benifit from classes if we did it this way
#To make these set up automaticall when we creat the employee 
#we are going to use a special init method
#so inside of our employee class we are going to create this special 
#init method. You can think of this method as initialize and if yo 
#are comming from another language you can think of it as a constructor

#when we create a method in the class they receive the instance as the first argument automatically
# by convention we should call the instance self
#you call it whatever you want but it is better to stick to the convention and use self

# after self we can specify what other arguments we want to accept 
#so we can accept the first, last, email and pay
#see class_example_0_b  to understand more


