#https://www.journaldev.com/14623/python-multiple-inheritance
# Resolving the Conflicts with python multiple inheritance
# Let’s have a look at another example.


		
class A:  
    def __init__(self):  
        self.name = 'John'  
        self.age = 23  
  
    def getName(self):  
        return self.name  
  
  
class B:  
    def __init__(self):  
        self.name = 'Richard'  
        self.id = '32'  
  
    def getName(self):  
        return self.name  
  
  
class C(A,B):  
    def __init__(self):  
        A.__init__(self)  
        B.__init__(self)  
  
    def getName(self):  
        return self.name  
  
C1 = C()  
print(C1.getName())  
#Class C inherits both A and B. And both of them has an attribute ‘name’. 
# From which class the value of name will be inherited in C? Is it from A or B? What do you think? Well, the output is:

# The name when printed is ‘Richard’ instead of ‘John’. Let’s try to understand what’s happening here. 
# In the constructor of C, the first constructor called is the one of A.
# So, the value of name in C becomes same as the value of name in A. 
# But after that, when the constructor of B is called, the value of name in C is overwritten by the value of name in B. 
# So, the name attribute of C retains the value ‘Richard’ when printed. The result would be same even if we declared class C as:
# Class C(B, A):
# The hierarchy becomes completely depended on the order of __init__() calls inside the subclass.
#  To deal with it perfectly, there is a protocol named MRO (Method Resolution Order).