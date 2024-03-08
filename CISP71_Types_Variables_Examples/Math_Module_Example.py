#https://www.w3schools.com/python/module_math.asp

import math

num = 49
num_sqrt = math.sqrt(num)


base = float(input('Enter initial savings: '))
print()

rate = float(input('Enter annual interest % rate: '))
print()

years = int(input('Enter years that pass: '))
print()

total = base * math.pow(1 + (rate / 100), years)

print ('Savings after', years, 'years is {0:8.2f}'.format(total) )