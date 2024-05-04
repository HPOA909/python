#import os we do not have to install anything it is a built in module
import os
from datetime import datetime

#To print operating system name
#Currently, it registers 'posix', 'nt', 'os2', 'ce', 'java' and 'riscos'.
print(os.name)   



# #to display all the attributes and methods that we have access to in this module
# print(dir(os))

# #print the current directory that we are in
# #getcwd -- cwd stands for current working directory
# print(os.getcwd())

# #if we want to navigate to another location  note chdir stands for change directory
# os.chdir('c:/Users/szaki5/Desktop/')
# print(os.getcwd())

# #display files and folders in the current directory
# #we will use a method listdir
# print(os.listdir())

# #list the files and folders in a particular path
# print (os.listdir('d:/'))

#let us navigate to our desktop 
#please change the following path to your desktop
#note we are using forward slash
os.chdir('C:/Users/szaki5/Desktop')

#let us make sure that we are there usind cwd
print(os.getcwd())

# #let us create a new folder on our desktop
# #there are two methods to do that mkdir and makedirs
# #makedirs allows you to create sublevel directories at the same step you do not have to have
# #the parent already there to create the child directory

# # os.mkdir('python_fun')
# os.makedirs('python_lessons/lesson1')

#to remove directories 
#we have two methods to do that 
#rmdir which will not remove intermediate directories
#removedirs which will remove intermediate directories

# #note in real world application it is perferrable to use rmdir better than removedirs 
# #to make sure that you are deleting the required directory
# os.removedirs('python_lessons/lesson1')

# #rename a file or folder
# #there is a method rename that takes two arguments original file name then the new file name
# #let us say I have file on my desktop with the name happy_python.txt and I want to rename it to 
# #having_fun_python.txt
# os.rename('happy_python.txt','having_fun_python.txt')

# #printing information about a file **os.stat()
# #let us say I want to print information about having_fun_python.txt
# #we can use os.stat
# print(os.stat('having_fun_python.txt'))

# #size, mtime=last modification time-this will give you timestamp
# #to display the actual date time format
# #you need to from datetime import datetime
# #create a variable
# mod_time=os.stat('having_fun_python.txt').st_mtime
# print(datetime.fromtimestamp(mod_time))

# # if you want to traverse the directory tree and print all of the directories and the
# # files then you can use the OS dot walk method so OS dot Walk is a generator that yields a couple of three values as its walking the directory tree so for each directory that it sees it yields the directory path the direct within that path and the files within
# # that path

# for dirpath, dirnames, filenames in os.walk('C:/Users/szaki5/Desktop'):
#     print('Current Path: ',dirpath)
#     print('Directories: ',dirnames)
#     print('Files: ', filenames)
#     print()
    

