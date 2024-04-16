""" #Create a class student and create object of that class
class Student:
    pass
#create an instance of this class
student1=Student()
student2=Student()
#assign values to the attribute

student1.first="Sam" """

""" class Student:
    num_of_students=0
    enrollmentFees=45

    def __init__ (self, first, last, gpa):
        self.first = first
        self.last = last
        self.gpa = gpa
        self.email = first+'.'+last+"@gmail.com"
        Student.num_of_students += 1

    def rosterName (self):
        return '{} {}'.format(self.last, self.first)

    def enrollment (self):
        return '{} enrollment fees'.format(Student.enrollmentFees)

student1=Student("Sam", "Mark", 8.0)
student2=Student("Shelby", "Howard", 9.9) """

""" class Customer :
    customerCount = 0

    def __init__ (self, name, accountNumber, balance):
        self.name = name
        self.accountNumber = accountNumber
        self.balance = balance
        Customer.customerCount += 1

    def displayCount(self):
        print ("Total number of customers: %d "%Customer.customerCount)

    def displayCustomer (self):
        print("Customer Info:")
        print("Name: ", self.name, "Account Number ",self.accountNumber) """

#using instranciation to create a variable using the student class

class Student:
    num_of_students=0 #Class variable
    def __init__ (self):
        self.name=''
        self.gpa=0
        #Increment the number of students
        Student.num_of_students += 1
#First instance
student1=Student()
print("First Step")
print(student1.name)
print(student1.gpa)

#Second instance
student2=Student()
#Update and modify all the attribute
student1.name="Sam"
student1.gpa=4.0

print("Second Step")
print(student1.name)
print(student1.gpa)

student2.name="Michael"
student2.gpa=4.0

print (student2.name)
print(student2.gpa)
print("Number of students:", Student.num_of_students)