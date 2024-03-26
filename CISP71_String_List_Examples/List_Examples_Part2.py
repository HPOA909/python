#reference https://www.w3resource.com/python-exercises/list/
#******
#*Exercise 1
#***************

#Write a Python program to sum all the items in a list
#reference https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.php
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))


#Write a Python program to get the largest number from a list
#reference https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-3.php
def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0]))

# Write a Python program to get the smallest number from a list.
#reference https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-4.php
def smallest_num_in_list( list ):
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
    return min
print(smallest_num_in_list([1, 2, -8, 0]))



#Write a Python program to remove duplicates from a list.
#reference https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-7.php
a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)

