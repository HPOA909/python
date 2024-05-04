#There is more than one way to read a file in Python. 
# If you need to extract a string that contains all characters in the file then we can
# use file.read()
path='C:/Users/szaki5/Desktop/CISP71_Files_OS_Examples/CISP71_Files_Examples/data/'
file = open(path+'Notes for p value and level of significance.txt', 'r') 
# This will print the content of the whole file
print (file.read())

