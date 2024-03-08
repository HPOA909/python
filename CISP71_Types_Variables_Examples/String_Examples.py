#https://www.w3schools.com/python/python_strings.asp

#Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])

#Slicing
#You can return a range of characters by using the slice syntax.

#Specify the start index and the end index, separated by a colon, to return a part of the string.
#Example
#Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])

#The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))

#The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

#The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#Check if the phrase "ain" is present in the following text:
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

#Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)