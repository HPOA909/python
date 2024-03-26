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