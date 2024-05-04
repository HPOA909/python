#This is the solution for exercise 12_8 in zybooks
file_name = input("Please enter file name: ")
bound_1 = input("Please enter bound_1: ")
bound_2 = input("Please enter bound_2: ")
path='C:/Users/szaki5/Desktop/CISP71_Files_OS_Examples/CISP71_Files_Examples/data/'
user_file = open(path+str(file_name))

output_list = user_file.readlines()

for x in output_list:
    x = x.strip('\n')
    if x >= bound_1 and x <= bound_2:
        print(x)


user_file.close()

 



