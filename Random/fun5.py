""" #defining a function
def greetings():
    print("Welcome to Python programming")

#call the function
greetings() """

""" #define a function with arguments
def my_function_with_args(username):
    print("Welcome, %s, to Python Programming"%(username))
    
#Call the function with parameter
my_function_with_args("Howard") """

""" #Define a function that it take arguments and provides a result
def product(num1, num2):
    return(num1,num2)

#To call this function, you should have it in expression
num1=5
num2=6
print("First number is:", num1)
print("Second number is:", num2)
print("The product is:", product(num1,num2)) """

""" #Define a function that will receive the first and last names and print roster and full names
def full_roster_name(finame,lasname):
    print("Full name is:",finame+' '+lasname)
    print("Roster name:",lasname,",",finame)

#call the function
full_roster_name("Sam","John") """

""" #Working with arguments program
def children(child1,child2,child3):
    print("The youngest child is "+child3)

#Call the function proving the wrong number of parameter
children(child1="Sam",child2="Jack",child3="Sue") """

""" #Work with default values for parameters
def studentInfo(name, age, major, city="Walnut"):
    print("Student name: ",name)
    print("Student age: ", age)
    print("Student major: ", major)
    print("Student city: ", city)

studentInfo("Sam",20,"Networking") """

""" #Working with a list as an argument for the function
def shoppingList(costco_list):
    for item in costco_list:
        print(item)

#Create the list
costco_list = ["Milk", "Cake", "Shrimps", "Strawberries"]
shoppingList(costco_list) """

""" def myfunc():
  x = 300
  print(x)

myfunc() """

""" x = 300
def myfunc6():
  x = 200
  print(x)
myfunc6()

print(x)
x=x+400
print(x) """

""" def calc_circle_area(circle_diameter):
    pi_val = 3.14159265
    circle_radius = circle_diameter / 2.0
    circle_area = pi_val * circle_radius * circle_radius
    return circle_area
 	
def pizza_calories(pizza_diameter):
    calories_per_square_inch = 16.7    # Regular crust pepperoni pizza
    total_calories = calc_circle_area(pizza_diameter) * calories_per_square_inch
    return total_calories
	
print('12 inch pizza has {:.2f} calories.'.format(pizza_calories(12.0)))
print('14 inch pizza has {:.2f} calories.'.format(pizza_calories(14.0))) """

""" #create a function that take the score of exam and return the letter grade
#define function
def grades(grades_exam):
    if (grades_exam >= 90):
        LG=print("Letter grade: A")
    elif (grades_exam >= 80):
        LG=print("Letter grade: B")
    elif (grades_exam >= 70):
        LG=print("Letter grade: C")
    elif (grades_exam >= 60):
        LG=print("Letter grade: D")
    else:
        LG=print("Letter grade F")
    return LG

# Call the function
grades(98) """

""" # Example 1: Printing a formatted string
name = "Alice"
age = 25
print("%s is %d years old." % (name, age))
# Output: Alice is 25 years old.

# Example 2: Printing a formatted string with a floating-point value
price = 19.99
print("The price is $%.2f." % price)
# Output: The price is $19.99. """

""" name="Sam"
age=23
enrollmenatFees=70

print("%s is %d years old. Enrollment fees $%.2f"%(name,age,enrollmenatFees))

print("{} is {} years old. Enrollment fees ${:.2f}".format(name,age,enrollmenatFees)) """

""" # Example 1: Printing a formatted string using 'str.format()'
name = "Bob"
age = 30
print("{} is {} years old.".format(name, age))
# Output: Bob is 30 years old.

# Example 2: Printing a formatted string with named arguments
product = "Python Course"
price = 99.99
print("{name} costs ${price:.2f}.".format(name=product, price=price))
# Output: Python Course costs $99.99. """

""" name="Jack"
age=18
fees=29.95

print(f'{name} is {age} years old. The fees for the club is ${fees:.2f}') """

""" basicPay=6000
sales=400
COMMISSION=.10

def grossPay(basicPay,sales):
    return basicPay * sales * COMMISSION

print("Your basic pay: ", basicPay)
print("Your sales: ", sales)
print("Your dross pay: ", grossPay(basicPay,sales)) """

""" def studentInfo(name,age,major,city):
    print("Student info: name: %s age: %d major: %s city: %s"%(name,age,major,city))

studentInfo("Sam",23,"Networking","Walnut") """

""" def studentInfo(name,age,major,city="Walnut"):
    print("Student info: name: %s age: %d major: %s city: %s"%(name,age,major,city))

studentInfo("Sam",23,"Networking") """

""" #Get the area of a circle
#radius
#create a function that will take the circle_diamater and return the area
#note PI is constant
#recall radius = diameter/2.0

def calc_circle_area(circle_diamater):
    #define a constant for pi_val
    pi_val = 3.14159265
    #declare the radius
    radius = circle_diamater/2.0
    #calculate the area
    circle_area = pi_val * (radius *radius)
    return circle_area

#Calories per sq in 16.7
#create a function to calculate the calories in pizza diameter
#total calories = area * cpi

def pizza_calories(pizza_diameter):
    #declare a constant for calories per sq in
    calories_per_square_inch = 16.7
    #total_calories = area * calories per sq in
    # call the function that will get the area
    total_calories = calc_circle_area(pizza_diameter) * calories_per_square_inch
    return total_calories

print(pizza_calories(12)) """

""" centimeters_per_inch = 2.54
inches_per_foot = 12

def height_US_to_centimeters(feet, inches):
    Converts a height in feet/inches to centimeters.
    total_inches = (feet * inches_per_foot) + inches  # Total inches
    centimeters = total_inches * centimeters_per_inch
    return centimeters

feet = int(input('Enter feet: '))
inches = int(input('Enter inches: '))

print('Centimeters:', height_US_to_centimeters(feet, inches)) """

""" def ebay_sale(price):
    if price > 50 and price <=1000:
        totalPrice= .50 + price + price * .05
    elif price <=50:
        totalPrice= .50 + price + price * .13
    else:
        totalPrice = .50 + price + price * .02
    return totalPrice

print(ebay_sale(99)) """