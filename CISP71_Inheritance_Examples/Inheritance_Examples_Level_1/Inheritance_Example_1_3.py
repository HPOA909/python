#Reference https://www.programiz.com/python-programming/multiple-inheritance
#Multiple inheritance

"""
 Desc:
  Python program to demonstrate the diamond problem
  (a.k.a. Multiple Inheritance)
"""

# Parent class 1
class TeamMember(object):                   
   def __init__(self, name, uid): 
      self.name = name 
      self.uid = uid 
  
# Parent class 2
class Worker(object):                 
   def __init__(self, pay, jobtitle): 
      self.pay = pay 
      self.jobtitle = jobtitle 
  
# Deriving a child class from the two parent classes
class TeamLeader(TeamMember, Worker):         
   def __init__(self, name, uid, pay, jobtitle, exp): 
      self.exp = exp 
      TeamMember.__init__(self, name, uid) 
      Worker.__init__(self, pay, jobtitle)
      print("Name: {}, Pay: {}, Exp: {}".format(self.name, self.pay, self.exp))

TL = TeamLeader('Jake', 10001, 250000, 'Scrum Master', 5)