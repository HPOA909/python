#Reference: https://www.journaldev.com/14454/python-custom-exception
#Python Custom Exception using assert statement
#Using assert statement you can initially create your own exception.
#Basically assert statement check for a condition.
#If the condition is not met then it will throw AssertionError.
#Suppose you wrote a function where you take age as an argument. 
#You don’t want to let programmers use the function if the age is less the 18. So the function would be.

def input_age(age):
    try:
        assert int(age) > 18
    except ValueError:
       return 'ValueError: Cannot convert into int'
    else:
       return 'Age is saved successfully'


print(input_age('23'))  # This will print
print(input_age(25))  # This will print
print(input_age('nothing'))  # This will raise ValueError which is handled
print(input_age('18'))  # This will raise AssertionError and the the program collapse
print(input_age(43))  # This will not print
