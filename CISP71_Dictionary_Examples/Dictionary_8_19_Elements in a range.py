#8.19 LAB: Elements in a range
#   Write a program that first gets a list of integers from input. That list is followed by two more integers representing lower and upper bounds of a range. Your program should output all integers from the list that are within that range (inclusive of the bounds).
# Ex: If the input is:
# 25 51 0 200 33
# 0 50
# the output is:
# 25 0 33 
# The bounds are 0-50, so 51 and 200 are out of range and thus not output.
# For coding simplicity, follow each output integer by a space, even the last one. Do not end with newline.

#grab user input and assign it to string
user_input = input()

#split user input into a list of tokens  
tokens = user_input.split() 

#Iterate through the tokens list and convert each item to an integer 
#generate a new list of those integers integer_list
integer_list = [int(a) for a in tokens]  

#now after you got the list of integers prompt the user to enter two more number min and max value
user_input = input()

#split user input to tokens
tokens = user_input.split() 

#convert the first element of tokens . element with index 0 of this list to an integer 
min_val = int(tokens[0])

#convert the second element of the tokens list to an integer
max_val = int(tokens[1])

#iterate through the integer_list elements checking if the item is between the min and max 
#if true print it
for i in range(len(integer_list)):
    if (integer_list[i] >= min_val) and (integer_list[i] <= max_val):
        print(integer_list[i], end=" ")
        
        