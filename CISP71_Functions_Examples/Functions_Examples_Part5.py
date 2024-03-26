#6.10 Scope of variables and functions
#Variable and function scope
#A variable or function object is only visible to part of a program, known as the object's scope.
# When a variable is created inside a function, the variable's scope is limited to inside that function.
#  In fact, because a variable's name does not exist until bound to an object, 
# the variable's scope is actually limited to after the first assignment of the variable
#  until the end of the function. The following program highlights the scope of variable total_inches.
centimeters_per_inch = 2.54
inches_per_foot = 12

def height_US_to_centimeters(feet, inches):
    """ Converts a height in feet/inches to centimeters."""
    total_inches = (feet * inches_per_foot) + inches  # Total inches
    centimeters = total_inches * centimeters_per_inch
    return centimeters

feet = int(input('Enter feet: '))
inches = int(input('Enter inches: '))

print('Centimeters:', height_US_to_centimeters(feet, inches))
#Local variable scope extends from assignment to end of function. Global variable scope extends to end of file.