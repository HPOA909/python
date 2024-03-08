#getting user input and converting data type
miles = float(input('Enter a distance in miles: '))

#calculations
hours_to_fly = miles / 500.0
hours_to_drive = miles / 60.0

#printing the results
print(miles, 'miles would take:')
print(hours_to_fly, 'hours to fly')
print(hours_to_drive, 'hours to drive')

#let us improve the printing
print("Formatted print")
print('{0:8.2f} miles would take:'.format(miles))
print('{0:8.2f} hours to fly:'.format(hours_to_fly))
print('{0:8.2f} hours to drive:'.format(hours_to_drive))