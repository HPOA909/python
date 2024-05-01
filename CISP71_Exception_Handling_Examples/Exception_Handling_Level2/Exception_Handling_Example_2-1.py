#Reference 
#Zybooks: 10.1.2: BMI example with exception handling using try/except.
#If the user entered a weight by writing out "One-hundred fifty", instead of giving a number such as "150",
# This would caused the int() function to produce an exception of type ValueError. The exception causes the program to terminate.
# Commonly, a program should gracefully handle an exception and continue executing, 
# instead of printing an error message and stopping completely. Code that potentially may produce an exception is placed in a try block.
# If the code in the try block causes an exception, then the code placed in a following except block is executed. 
# Consider the program below, which modifies the BMI program to handle bad user input.


user_input = ''
while user_input != 'q':
    try:
        weight = int(input("Enter weight (in pounds): "))
        height = int(input("Enter height (in inches): "))

        bmi = (float(weight) / float(height * height)) * 703
        print('BMI:', bmi)
        print('(CDC: 18.6-24.9 normal)\n')  # Source www.cdc.gov
    except:
        print('Could not calculate health info.\n')

    user_input = input("Enter any key ('q' to quit): ")
