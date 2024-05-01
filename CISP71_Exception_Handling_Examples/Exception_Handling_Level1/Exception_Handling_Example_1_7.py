#Reference https://www.journaldev.com/14454/python-custom-exception
#Python Custom Exception Class
#Python allow programmers to create their own exception class.
# Exceptions should typically be derived from the Exception class, either directly or indirectly.
# In the following example, we create custom exception class UnderAge that is derived from the base class Exception.
#Again, in another method we raised the UnderAge exception if the condition is not met.
# The following code will give you some insight about the idea.



class UnderAge(Exception):
   pass

def verify_age(age):
   if int(age) < 18:
       raise UnderAge
   else:
       print('Age: '+str(age))

# main program
verify_age(23)  # won't raise exception
verify_age(17)  # will raise exception