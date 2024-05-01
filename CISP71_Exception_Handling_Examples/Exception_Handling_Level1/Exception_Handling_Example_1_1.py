#Reference 
#https://www.datacamp.com/community/tutorials/exception-handling-python?utm_source=adwords_ppc&utm_campaignid=1565261270&utm_adgroupid=67750485268&utm_device=m&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=295208661496&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9031211&gclid=CjwKCAjw0On8BRAgEiwAincsHCsU3lum68H1IJ0MRep0AKDx1uYB8vPrcbLAd5TmYloriTppkajpMxoCD7AQAvD_BwE
# difference between an error and an exception.
# Errors cannot be handled, while Python exceptions can be handled at the run time.
#An Error might indicate critical problems that a reasonable application should not try to catch,
# while an Exception might indicate conditions that an application should try to catch.
# Errors are a form of an unchecked exception and are irrecoverable like an OutOfMemoryError,
# which a programmer should not try to handle.


#An exception object is created when a Python script raises an exception.
# If the script explicitly doesn't handle the exception, the program will be forced to terminate abruptly.

#https://docs.python.org/2/library/exceptions.html#exception-hierarchy

#Try: It will run the code block in which you expect an error to occur.
# Except: Here, you will define the type of exception you expect in the try block (built-in or custom).
# Else: If there isn't any exception, then this block of code will be executed (consider this as a remedy or a fallback option if you expect a part of your script to produce an exception).
# Finally: Irrespective of whether there is an exception or not, this block of code will always be executed.

#Example 1-1-a
#Zero Division
#When the divisor (second argument of the division) or the denominator is zero, then the resultant raises a zero division error.
try:  
    a = 100 / 0
    print (a)
except ZeroDivisionError:  
        print ("Zero Division Exception Raised." )
else:  
    print ("Success, no error!")

#Example 1-1-b
#OverFlow Error
#The Overflow Error is raised when the result of an arithmetic operation is out of range.
#OverflowError is raised for integers that are outside a required range.

try:  
    import math
    print(math.exp(1000))
except OverflowError:  
        print ("OverFlow Exception Raised.")
else:  
    print ("Success, no error!")
    
    
#Example 1-1-c
#Attribute Error
#When a non-existent attribute is referenced, and when that attribute reference or assignment fails, an attribute error is raised.

class Attributes(object):
    a = 2
    print (a)

try:
    object = Attributes()
    print (object.attribute)
except AttributeError:
    print ("Attribute Exception Raised.")
    
#Example 1-1-d    
#Index Error
#When you are trying to access an index (sequence) of a list that does not exist in that list or is out of range of that list,
# an index error is raised.

try:  
    a = ['a', 'b', 'c']  
    print (a[4])  
except LookupError:  
    print ("Index Error Exception Raised, list index out of range")
else:  
    print ("Success, no error!")   
    
#Example 1-1-e
#Type Error
# Type Error Exception is raised when two different or unrelated types of operands or objects are combined.   

try:
    a = 5
    b = "DataCamp"
    c = a + b
except TypeError:
    print ('TypeError Exception Raised')
else:
    print ('Success, no error!')
    
#Example 1-1-f
#Value Error
#Value error is raised when the built-in operation or a function receives an argument that has a correct type but invalid value.

try:
    print (float('DataCamp'))
except ValueError:
    print ('ValueError: could not convert string to float: \'DataCamp\'')
else:
    print ('Success, no error!')
    

