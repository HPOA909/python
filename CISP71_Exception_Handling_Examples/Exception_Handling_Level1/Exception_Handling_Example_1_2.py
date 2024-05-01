#Python Custom Exceptions
#Reference: https://www.datacamp.com/community/tutorials/exception-handling-python
#As studied in the previous section of the tutorial, Python has many built-in exceptions that you can use in your program.
#Still, sometimes, you may need to create custom exceptions with custom messages to serve your purpose.
#You can achieve this by creating a new class, which will be derived from the pre-defined Exception class in Python.

class UnAcceptedValueError(Exception):   
    def __init__(self, data):    
        self.data = data
    def __str__(self):
        return repr(self.data)
    
#https://www.programiz.com/python-programming/methods/built-in/repr
#The repr() function returns a printable representation of the given object.


Total_Marks = int(input("Enter Total Marks Scored: "))
try:
    Num_of_Sections = int(input("Enter Num of Sections: "))
    if(Num_of_Sections < 1):
        raise UnAcceptedValueError("Number of Sections can't be less than 1")
except UnAcceptedValueError as e:
    print ("Received error:", e.data)
