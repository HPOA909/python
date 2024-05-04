""" try:  
    a = ['a', 'b', 'c']  
    print (a[4])
except LookupError:
    print("You have entered an inproper index")
else:
    print("Index found!") """

try:
    a = 5
    b = "DataCamp"
    c = a + b
except TypeError:
    print ('TypeError Exception Raised')
else:
    print ('Success, no error!')