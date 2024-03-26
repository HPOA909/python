#reference https://www.w3schools.com/python/python_functions.asp
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
# Creating a Function
# In Python a function is defined using the def keyword
def my_function():
  print("Hello from a function")
  
#To call a function, use the function name followed by parenthesis:

my_function()

# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
# The following example has a function with one argument (fname). 
# When the function is called 
# We pass along a first name, which is used inside the function to print the full name

def  my_function2(fname):
      print(fname + " Refsnes")

my_function2("Emil")
my_function2("Tobias")
my_function2("Linus")

#Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: 
# information that are passed into a function.
# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.
# Number of Arguments
# By default, a function must be called with the correct number of arguments.
# Meaning that if your function expects 2 arguments, you have to call the 
# function with 2 arguments, not more, and not less.

# Example
# This function expects 2 arguments, and gets 2 arguments
def my_function1(fname, lname):
    print(fname + " " + lname)
    

def my_function3(child3, child2, child1):
      print("The youngest child is " + child3)

my_function3(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#Default Parameter Value
# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value 

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.),
# and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function 


def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Return Values
# To let a function return a value, use the return statement 
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

