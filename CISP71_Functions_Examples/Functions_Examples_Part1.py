#Reference https://www.learnpython.org/en/Functions
#What are Functions?
# Functions are a convenient way to divide your code into useful blocks, 
# allowing us to order our code, make it more readable, 
# reuse it and save some time. Also functions are a key way to define 
# interfaces so programmers can share their code.


#Functions in python are defined using the block keyword "def",
# followed with the function's name as the block's name. 
#The following function does not take any argument and does not return anything
#****Example 1***
def my_function():
    print("Hello From My Function!")
    
 #How to call this function
print("Calling my_function")
my_function()

#***Example 2 **
#Functions may also receive arguments 
# (variables passed from the caller to the function)


#Functions may return a value to the caller, using the keyword- 'return' 
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))
    
#Functions may return a value to the caller, using the keyword- 'return' 
def sum_two_numbers(a, b):
    return a + b

#How do you call functions in Python? 
# Define our 3 functions
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)  
    