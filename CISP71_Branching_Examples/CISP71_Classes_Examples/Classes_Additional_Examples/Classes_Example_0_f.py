#Reference https://www.tutorialspoint.com/python/python_classes_objects.htm
#Following is the example of a simple Python class −



class Employee:
   '''Common base class for all employees'''
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)