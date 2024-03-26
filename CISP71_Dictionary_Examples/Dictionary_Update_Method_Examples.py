#python dictionary update method
#https://www.geeksforgeeks.org/python-dictionary-update-method/
# Python program to show working 
# of update() method in Dictionary 

# Dictionary with three items 
Dictionary1 = { 'A': 'Geeks', 'B': 'For', } 
Dictionary2 = { 'B': 'Geeks' } 

# Dictionary before Updation 
print("Original Dictionary:") 
print(Dictionary1) 

# update the value of key 'B' 
Dictionary1.update(Dictionary2) 
print("Dictionary after updation:") 
print(Dictionary1) 


##another example
## Python program to show working 
# of update() method in Dictionary 

# Dictionary with single item 
Dictionary1 = { 'A': 'Geeks'} 

# Dictionary before Updation 
print("Original Dictionary:") 
print(Dictionary1) 

# update the Dictionary with iterable 
Dictionary1.update(B = 'For', C = 'Geeks') 
print("Dictionary after updation:") 
print(Dictionary1) 

#*****************
#***Python – Update dictionary with other dictionary
#*****************************************************
#Method #1 : Using loop
# Python3 code to demonstrate working of 
# Update dictionary with other dictionary 
# Using loop 

# initializing dictionaries 
test_dict1 = {'gfg' : 1, 'best' : 2, 'for' : 4, 'geeks' : 6} 
test_dict2 = {'for' : 3, 'geeks' : 5} 

# printing original dictionaries 
print("The original dictionary 1 is : " + str(test_dict1)) 
print("The original dictionary 2 is : " + str(test_dict2)) 

# Update dictionary with other dictionary 
# Using loop 
for key in test_dict1: 
	if key in test_dict2: 
		test_dict1[key] = test_dict2[key] 

# printing result 
print("The updated dictionary is : " + str(test_dict1)) 


#Method #2 : Using dictionary comprehension
# Python3 code to demonstrate working of 
# Update dictionary with other dictionary 
# Using dictionary comprehension 

# initializing dictionaries 
test_dict1 = {'gfg' : 1, 'best' : 2, 'for' : 4, 'geeks' : 6} 
test_dict2 = {'for' : 3, 'geeks' : 5} 

# printing original dictionaries 
print("The original dictionary 1 is : " + str(test_dict1)) 
print("The original dictionary 2 is : " + str(test_dict2)) 

# Update dictionary with other dictionary 
# Using dictionary comprehension 
res = {key : test_dict2.get(key, val) for key, val in test_dict1.items()} 

# printing result 
print("The updated dictionary is : " + str(res)) 
