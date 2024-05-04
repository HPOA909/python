#Another way to read a file is to call a certain number of characters 
# like in the following code the interpreter will read the first 100 characters 
# of stored data and return it as a string:
path='C:/Users/szaki5/Desktop/CISP71_Files_OS_Examples/CISP71_Files_Examples/data/'
file = open(path+'Notes for p value and level of significance.txt', 'r') 
# Python code to illustrate read() mode character wise 

print (file.read(100) )


