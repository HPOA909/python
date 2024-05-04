#This is the solution for exercise 12_9 in zybooks
import csv
file_name = input("Please enter file name: ")
path='C:/Users/szaki5/Desktop/CISP71_Files_OS_Examples/CISP71_Files_Examples/data/'
word_list = []

with open(path+str(file_name), 'r') as csvfile:
    user_file = csv.reader(csvfile, delimiter=',')
    
    for row in user_file:
        for index in range(len(row)):
            if row[index] not in word_list:
                print('{} {}'.format(row[index], row.count(row[index])))
                word_list.append(row[index])
