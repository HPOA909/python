#https://www.w3schools.com/python/python_lists.asp
#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered and unindexed. No duplicate members.
#Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#Create a List:

thislist = ["apple", "banana", "cherry"]
print(thislist)

#You access the list items by referring to the index number:
#Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Range of Indexes
#You can specify a range of indexes by specifying where to start and where to end the range.

#When specifying a range, the return value will be a new list with the specified items.
#Example
#Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#The search will start at index 2 (included) and end at index 5 (not included).
#Remember that the first item has index 0.
#By leaving out the start value, the range will start at the first item:

#This example returns the items from the beginning to "orange":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#This example returns the items from "cherry" and to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Range of Negative Indexes
#Specify negative indexes if you want to start the search from the end of the list:
#This example returns the items from index -4 (included) to index -1 (excluded)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#To change the value of a specific item, refer to the index number:
#Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Print the number of items in the list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#To add an item at the specified index, use the insert() method:
#Insert an item as the second position:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Remove Item
#There are several methods to remove items from a list:
#The remove() method removes the specified item:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
