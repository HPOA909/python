#8.18 LAB: Middle item
#   Given a sorted list of integers, output the middle integer. Assume the number of integers is always odd.
#   Ex: If the input is:
#   2 3 4 8 11
#   the output is:
#   4
#   The maximum number of inputs for any test case should not exceed 9. If exceeded, output "Too many inputs".
#   Ex: If the input is:
#   10 20 30 40 50 60 70 80 90 100 110
#   The output is 
#   Too many inputs
#Hint: First read the data into a list. Then, based on the list's size, find the middle item.

# User inputs string w/ numbers
user_input = input()

# Split into separate strings and convert to integers
tokens = user_input.split()  
data_set = [int(a) for a in tokens]

num_values = len(data_set)
if num_values > 9 :  # Too many inputs
    print('Too many inputs')
else:                           # Even number, so get middle two values
    mid_index = num_values // 2 
    print(data_set[mid_index])
