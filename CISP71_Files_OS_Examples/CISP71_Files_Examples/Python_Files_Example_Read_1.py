#We use open () function in Python to open a file in read or write mode.
#open ( ) will return a file object. 
# To return a file object we use open() function along with two arguments, 
# that accepts file name and the mode, whether to read or write.
# So, the syntax being: open(filename, mode). 
# There are three kinds of mode, that Python provides and how files can be opened:

# "r", for reading.
# "w", for writing.
# "a", for appending.
# "r+", for both reading and writing

# If not passed, then Python will assume it to be “ r ” by default
# a file named "Notes for p value and level of significance", will be opened with the reading mode. 

#The open command will open the file in the read mode and the for loop will print each line present in the file.


path='C:/Users/szaki5/Desktop/CISP71_Files_OS_Examples/CISP71_Files_Examples/data/'
file = open(path+'Notes for p value and level of significance.txt', 'r') 
# This will print every line one by one in the file 
for each in file: 
	print (each) 

