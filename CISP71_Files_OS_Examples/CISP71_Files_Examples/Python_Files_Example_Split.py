# split() using file handling
# We can also split lines using file handling in Python. 
# This splits the variable when space is encountered. 
# You can also split using any characters as we wish. 


path=path='C:/Users/szaki5/Desktop/CISP71_Files_OS_Examples/CISP71_Files_Examples/data/'
with open(path+"file.txt", "r") as file: 
	data = file.readlines() 
	for line in data: 
		word = line.split() 
		print (word)