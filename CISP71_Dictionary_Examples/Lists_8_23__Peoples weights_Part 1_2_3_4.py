#reference Lab 8.23 Zybooks
# (1) Prompt the user to enter four numbers, each corresponding to a person's weight in pounds. Store all weights in a list. Output the list.
# (2) Output the average of the list's elements with two digits after the decimal point. Hint: Use a conversion specifier to output with a certain number of digits after the decimal point. 
# (3) Output the max list element with two digits after the decimal point. 
# (4) Prompt the user for a number between 1 and 4. Output the weight at the user specified location and the corresponding value in kilograms. 1 kilogram is equal to 2.2 pounds. 
# (5) Sort the list's elements from least heavy to heaviest weight.

#(1): Prompt for four weights. Add all weights to a list. Output list.
people_weights = []
num_weights = 4

for i in range(num_weights):
   single_weight = float(input('Enter weight {}:\n'.format(i+1)))
   people_weights.append(single_weight)

print('Weights:', people_weights)


#(2): Output average of weights.
avg_weight = sum(people_weights)/len(people_weights)
print('\nAverage weight: {:.2f}'.format(avg_weight))


#(3): Output max weight from list.
print('Max weight: {:.2f}'.format(max(people_weights)))

#(4): Prompt the user for a list index and output that weight in pounds and kilograms.
index = int(input('\nEnter a list location (1 - 4):\n'))
chosen_weight = people_weights[index-1]
print('Weight in pounds: {:.2f}'.format(chosen_weight))
print('Weight in kilograms: {:.2f}'.format(chosen_weight/2.2))


