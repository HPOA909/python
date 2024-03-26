#6.3.4: Program with a function to convert height in feet/inches to centimeters.
CM_PER_INCH = 2.54
INCHES_PER_FOOT = 12

def height_US_to_cm(feet, inches):
    """Converts height in feet/inches to centimeters"""
    total_inches = feet * INCHES_PER_FOOT + inches
    cm = total_inches * CM_PER_INCH
    return cm

feet = 6
inches = 4
	
centimeters = height_US_to_cm(feet, inches)
print('Centimeters:', centimeters)

#6.3.5: Hierarchical function calls
# Hierarchical function calls
# A function's statements may include function calls, 
# known as hierarchical function calls or nested function calls. 
# Code such as user_input = int(input()) consists of such a hierarchical function call,
#  wherein the input() function is called and evaluates to a value that is then passed 
#  as an argument to the int() function.

def calc_circle_area(circle_diameter):
    pi_val = 3.14159265
    circle_radius = circle_diameter / 2.0
    circle_area = pi_val * circle_radius * circle_radius
    return circle_area
 	
def pizza_calories(pizza_diameter):
    calories_per_square_inch = 16.7    # Regular crust pepperoni pizza
    total_calories = calc_circle_area(pizza_diameter) * calories_per_square_inch
    return total_calories
	
print('12 inch pizza has {:.2f} calories.'.format(pizza_calories(12.0)))
print('14 inch pizza has {:.2f} calories.'.format(pizza_calories(14.0)))
