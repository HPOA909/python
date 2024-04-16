#Reference https://www.tutorialspoint.com/python/python_classes_objects.htm
#Reference https://www.youtube.com/watch?v=ZDa-Z5JzLYM
# Class − A user-defined prototype for an object that defines a set of attributes that characterize any object of the class. The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.
# Class variable − A variable that is shared by all instances of a class. Class variables are defined within a class but outside any of the class's methods. Class variables are not used as frequently as instance variables are.
# Data member − A class variable or instance variable that holds data associated with a class and its objects.
# Function overloading − The assignment of more than one behavior to a particular function. The operation performed varies by the types of objects or arguments involved.
# Instance variable − A variable that is defined inside a method and belongs only to the current instance of a class.
# Inheritance − The transfer of the characteristics of a class to other classes that are derived from it.
# Instance − An individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle.
# Instantiation − The creation of an instance of a class.
# Method − A special kind of function that is defined in a class definition.
# Object − A unique instance of a data structure that's defined by its class. An object comprises both data members (class variables and instance variables) and methods.
# Operator overloading − The assignment of more than one function to a particular operator.

###Why use classes###
# They allow us to logically group our data and functions in a way that's easy to 
# to reuse and also build upon if need be. 
# When we say data and functions that are associated with a specific class, we call those 
# attribures and methods
#Method is a function that is associated with a class

#Let us say we have a company and we want to represent our employees in our python code
#Each individual employee will have specific attributes and methods
#For example each employee is going to have name, email address,pay
#and also actions that they can perform 
#It will be nice to have a class that we could use a blueprint to create
#each employee so that we don't have to do this manually each time from scratch.

#if you wrote 
#class Employee:
# and nothing inside it you will get an error
#You can say
#class Employee:
#      pass
# to inform jupyter that you will add the code for that Employee class later on


#Difference between a class and an instance of a class
#A class is a blueprint for creating Instances 
#Each unique employee that we create using our Employee class is an instance of thei class
 
#for example

# class Employee:
#      pass
#  emp_1=Employee()
#  emp_2=Employee()
# print(emp_1)
# print(emp_2)


# So emp_1 and emp_2 each of these are going to be their own unique instances of the employee class

# let us try to print them you will see that each is an employee object
#and both are unique. Both have different locations here in memory now

#Instance variables contain data that is unique to each instance





 