#operators_precedence_example
#https://www.tutorialspoint.com/python/operators_precedence_example.htm
a = 20
b = 10
c = 15
d = 5
e = 0

e = ((a + b) * c) / d     # (30 * 15 ) / 5
print ("Value of ((a + b) * c) / d is ",  e)

x= (a + b) * (c / d);    # (30) * (15/5)
print ("Value of (a + b) * (c / d) is ", x)

y = a + (b * c) / d;      #  20 + (150/5)
print ("Value of a + (b * c) / d is ",  y)