#printing
x = 'hello'
print(x)

#declaring two variables and assigning values to them
age = 12
name = 'Sam'
major='CIS'

#Let us see how use print formatting
print("Method 1")
print('{} is a student. He is {} years old. His major is {}.'.format(name,age,major))

#another way for printing
print("Method 2")
print('{0} is a student. He is {1} years old. His major is {2}.'.format(name,age,major))

#why this is useful
print('{0} is a student. He is {1} years old. His major is {2}. {0} welcome to our Python course'.format(name,age,major))

#printing using variable names in the format
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))


#printing numbers 
print ("Art: {0:5d}, Price per Unit: {1:8.2f}". format(453, 59.058))

print ("Art: {a:5d}, Price: {p:8.2f}".format (a=789, p=79.058))
