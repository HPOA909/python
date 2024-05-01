
#The power of exceptions becomes even more clear when used within functions.
#If an exception is raised within a function and is not handled within that function,
# then the function is immediately exited and the calling function is checked for a handler, and so on up the function call hierarchy.
# The following program illustrates. Note the clarity of the normal code, which obviously "gets the weight, gets the height, and prints the BMI" – the error checking code does not obscure the normal code.

# 10.4.1: BMI example using exception-handling constructs along with functions.
def get_weight():
    weight = int(input('Enter weight (in pounds): '))
    if weight < 0:
        raise ValueError('Invalid weight.')
    return weight

def get_height():
    height = int(input('Enter height (in inches): '))
    if height <= 0:
        raise ValueError('Invalid height.')
    return height

user_input = ''
while user_input != 'q':
    try:
        weight = get_weight()
        height = get_height()

        bmi = (float(weight) / float(height * height)) * 703
        print('BMI:', bmi)
        print('(CDC: 18.6-24.9 normal)\n')
        # Source www.cdc.gov

    except ValueError as excpt:
        print(excpt)
        print('Could not calculate health info.\n')

    user_input = input("Enter any key ('q' to quit): ")