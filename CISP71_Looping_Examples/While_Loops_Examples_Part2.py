#reference https://www.geeksforgeeks.org/python-while-loops/
# Python program to illustrate 
# while loop 
count = 0
while (count < 3):	 
	count = count + 1
	print("Hello Geek") 

print() 

# checks if list still 
# contains any element 
a = [1, 2, 3, 4] 
while a: 
	print(a.pop()) 
 
# Python program to illustrate 
# Single statement while block 
count = 0
while (count < 5): count += 1; print("Hello Geek") 

# Loop Control Statements
# Loop control statements change execution from its normal sequence. When execution leaves a scope, all automatic objects that were created in that scope are destroyed. Python supports the following control statements.
# Continue Statement: It returns the control to the beginning of the loop

# Prints all letters except 'e' and 's' 
i = 0
a = 'geeksforgeeks'

while i < len(a): 
	if a[i] == 'e' or a[i] == 's': 
		i += 1
		continue
	print('Current Letter :', a[i]) 
	i += 1

#Break Statement: It brings control out of the loop
# break the loop as soon it sees 'e' 
# or 's' 
i = 0
a = 'geeksforgeeks'

while i < len(a): 
	if a[i] == 'e' or a[i] == 's': 
		i += 1
		break
	print('Current Letter :', a[i]) 
	i += 1


