#reference : https://www.w3schools.com/python/python_strings.asp
# String Literals
# String literals in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
#**Assign String to a Variable
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

a = "Hello"
print(a)
#*********************
#***Multiline Strings
#*********************

# You can assign a multiline string to a variable by using three quotes:
# You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#*************************
#*****Strings are Arrays
#*************************

# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.

#Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])

#***********************
#***Slicing
#************************

# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
# Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])


#*******************
#***Negative Indexing
#********************

# Use negative indexes to start the slice from the end of the string:
# Example
# Get the characters from position 5 to position 1 (not included), starting the count from the end of the string:

b = "Hello, World!"
print(b[-5:-2])


#*************************
#****String Length
#************************

# To get the length of a string, use the len() function.
# Example
# The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))


#*********************
#***String Methods
#**********************

# Python has a set of built-in methods that you can use on strings.
#---- The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#----The lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())

#---The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())


#---The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))

#---The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#---Check String
# To check if a certain phrase or character is present in a string, we can use the keywords in or not in.
# Example
# Check if the phrase "ain" is present in the following text:
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

#Example
# Check if the phrase "ain" is NOT present in the following text:
txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x) 

#***************
#***
#*****************

#String Concatenation
# To concatenate, or combine, two strings you can use the + operator

# Example
# Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)

# Example
# To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)


#*********************
#***String Format
#*****************

# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
# Example
# age = 36
txt = "My name is John, I am " + age
print(txt)

# But we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

# Example
# Use the format() method to insert numbers into strings:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

##Example

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


#**********************
#****Escape Character
#**********************

# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
#The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."

#**********************
#*Other Escape characters used in Python
#******************


# Code	Result	 
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

#****************************
#******Other string methods
#***************************

#reference https://www.w3schools.com/python/python_strings.asp

# Method	Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning	

txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)



txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)


txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)


txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")


#count()	Python String count() function returns the number of occurrences of a substring in the given string.
# Python String count() Method
# Example
# Return the number of times the value "apple" appears in the string:

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)


#The count() method returns the number of times a specified value appears in the string.

# Syntax
# string.count(value, start, end)
# Parameter Values
# Parameter	Description
# value	Required. A String. The string to value to search for
# start	Optional. An Integer. The position to start the search. Default is 0
# end	Optional. An Integer. The position to end the search. Default is the end of the string

# Search from position 10 to 24:

txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple", 10, 24)

print(x)


#Python String partition() Method

# Example
# Search for the word "bananas", and return a tuple with three elements:

# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"

txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)


