""" #Create a class name it MyEmployee
class MyEmployee:
    raise_amt = 1.9 #Class variable
    #Create __init__ method
    def __init__ (self, fName, lName, salary):
        self.fName=fName
        self.lName=lName
        self.salary=salary

    #Another method to return the full name
    def fullName(self):
        return '{} {}'.format(self.fName,self.lName)

    #another method to apply raise
    def apply_raise(self):
        self.salary=int(self.salary * self.raise_amt)

#Create a class name it Programmer
class Programmer(MyEmployee):
    raise_amt=2.0
    #Define init method
    def __init__ (self,fName, lName, salary, prog_lang):
        #Call super().__init__ to call
        super.__init__(fName,lName,salary)
        self.prog_lang=prog_lang

#Create a class name it Manager
class Manager(MyEmployee):
    #define init method
    def __init__ (self, fName,lName,salary,employees=None):
        super.__init__(fName,lName,salary)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp (self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

#create an instance of progammer
programmer_1=Programmer("Shalby","Howard",6000,"Python")
programmer_2=Programmer("Paul", "Hernadez", 6000, "Python")

#create an instance of manager
manager_1=Manager("Jesus","Christ", 9000,(programmer_1))
manager_2=Manager("Paul", "Saul", 9000, (programmer_2)) """

