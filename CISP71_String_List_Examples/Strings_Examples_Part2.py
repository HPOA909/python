#reference https://www.w3resource.com/python-exercises/string/

#****Exercise 1
#***************

#Write a Python program to count the number of characters (character frequency) in a string.
#Sample String : google.com'
#Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com'))

#reference for flow chart
#https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-2.php


#****Exercise 2
#*****************

# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. Go to the editor
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String
#Reference  https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-3.php
def string_both_ends(str):
    if len(str) < 2:
        return ''
    return str[0:2] + str[-2:]

print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))


#*****Exercise 3
#***************

# Write a Python function to reverses a string if it's length is a multiple of 4.
#Reference https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-20.php

def reverse_string(str1):
    if len(str1) % 4 == 0:
       return ''.join(reversed(str1))
    return str1

print(reverse_string('abcd'))
print(reverse_string('python'))