#Looping examples for python
#Reference https://www.learnpython.org/en/Loops
#Reference https://www.geeksforgeeks.org/python-for-loops/?ref=rp

#There are two types of loops in Python, for and while.
#The "for" loop
print("Example 1")
print("==========")
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
    
#For loops can iterate over a sequence of numbers using the "range" and "xrange" functions.
#The difference between range and xrange is that the range function returns a new list with numbers of that specified range, whereas xrange returns an iterator, which is more efficient. (Python 3 uses the range function, 
#which acts like xrange). Note that the range function is zero based.
# 
# Prints out the numbers 0,1,2,3,4
print("Example 2")
print("=========")
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)
#reference https://www.geeksforgeeks.org/python-for-loops/?ref=rp   
# For loops, in general, are used for sequential traversal. It falls under the category of definite iteration. Definite iterations means the number of repetitions is specified explicitly in advance. 
# Note: In python, for loops only implements the collection-based iteration. 
# For in loops
# For loops are used for sequential traversal. For example: traversing a list or string or array etc. In Python, there is no C style for loop, i.e., for (i=0; i<n; i++). There is “for in” loop which is similar to for each loop in other languages. Let us learn how to use for in loop for sequential traversals.
# Syntax: 

# for var in iterable:
#     # statements

# Python program to illustrate 
# Iterating over a list 
print("List Iteration") 
l = ["geeks", "for", "geeks"] 
for i in l: 
	print(i) 
		
# Iterating over a tuple (immutable) 
print("\nTuple Iteration") 
t = ("geeks", "for", "geeks") 
for i in t: 
	print(i) 
		
# Iterating over a String 
print("\nString Iteration")	 
s = "Geeks"
for i in s : 
	print(i) 
		
# Iterating over dictionary 
print("\nDictionary Iteration")	 
d = dict() 
d['xyz'] = 123
d['abc'] = 345
for i in d : 
	print("% s % d" %(i, d[i])) 

# Loop control statements change execution from its normal sequence. When execution leaves a scope, all automatic objects that were created in that scope are destroyed. Python supports the following control statements. 
# Continue Statement: It returns the control to the beginning of the loop.

# Prints all letters except 'e' and 's' 
for letter in 'geeksforgeeks': 
	if letter == 'e' or letter == 's': 
		continue
	print('Current Letter :', letter) 
	var = 10

#Break Statement: It brings control out of the loop.
for letter in 'geeksforgeeks': 
	
	# break the loop as soon it sees 'e' 
	# or 's' 
	if letter == 'e' or letter == 's': 
		break
	
print('Current Letter :', letter) 

# range() function
# range() is a built-in function of Python. It is used when a user needs to perform an action for a specific number of times. range() in Python(3.x) is just a renamed version of a function called xrange() in Python(2.x). The range() function is used to generate a sequence of numbers. 
# In simple terms, range() allows user to generate a series of numbers within a given range. Depending on how many arguments user is passing to the function, user can decide where that series of numbers will begin and end as well as how big the difference will be between one number and the next.range() takes mainly three arguments. 
# start: integer starting from which the sequence of integers is to be returned 
#  stop: integer before which the sequence of integers is to be returned. 
# The range of integers end at stop – 1. 
# step: integer value which determines the increment between each integer in the sequence 

# Python Program to 
# show range() basics 

# printing a number 
for i in range(10): 
	print(i, end=" ") 
print() 

# using range for iteration 
l = [10, 20, 30, 40] 
for i in range(len(l)): 
	print(l[i], end=" ") 
print() 

# performing sum of first 10 numbers 
sum = 0
for i in range(1, 10): 
	sum = sum + i 
print("Sum of first 10 numbers :", sum) 
