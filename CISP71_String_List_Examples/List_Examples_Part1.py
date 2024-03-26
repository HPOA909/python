#reference Python List/Array Methods 
#https://www.w3schools.com/python/python_ref_list.asp

#Python has a set of built-in methods that you can use on lists/arrays.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# Add an element to the fruits list:

fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")

# The append() method appends an element to the end of the list.
# Syntax
# list.append(elmnt)
# Parameter Values
# Parameter	Description
# elmnt	Required. An element of any type (string, number, object etc.)

#Add a list to a list:

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)


#The clear() method removes all the elements from a list.
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()

#The copy() method returns a copy of the specified list.
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()

#count()	Returns the number of elements with the specified value
#Return the number of times the value "cherry" appears int the fruits list:

fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)


#extend()	Add the elements of a list (or any iterable), to the end of the current list
#Add the elements of cars to the fruits list:
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)

#Add a tuple to the fruits list:

fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)

#index()	Returns the index of the first element with the specified value
#What is the position of the value "cherry":
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")


#What is the position of the value 32:
fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)

#insert()	Adds an element at the specified position
#Insert the value "orange" as the second element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")

#The insert() method inserts the specified value at the specified position.
# Syntax
# list.insert(pos, elmnt)
# Parameter Values
# Parameter	Description
# pos	Required. A number specifying in which position to insert the value
# elmnt	Required. An element of any type (string, number, object etc.)

#pop()	Removes the element at the specified position
#Remove the second element of the fruit list:

fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)

#The pop() method removes the element at the specified position.
# list.pop(pos)
# Parameter Values
# Parameter	Description
# pos	Optional. A number specifying the position of the element you want to remove, default value is -1, which returns the last item

#Return the removed element:

fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(1)

# Note: The pop() method returns removed value.

# remove()	Removes the first item with the specified value

# Remove the "banana" element of the fruit list:

fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")

#The remove() method removes the first occurrence of the element with the specified value.




