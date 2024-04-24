""" string1 = "*******MtSAC CIS Business Division********"
string2 = "Having fun."
string3 = string1.lstrip()
print(string1.lstrip("*")+string2)
print(string1.rstrip("*")+string2)
print(string1.strip("*")+string2)

txt = "50"

x = txt.zfill(4)

print(x) """

""" #Create a list
students_group1=["Ivan","Sun","Frank","Paul"]

students_group2=["Hilary", "Mark", "Krystopher","Mary"]

students_group1.append(students_group2)

print(students_group2) """

""" #Create a list
student1=["Sam","Paul","Hnery","Paul","Jack","Paul"]
print(student1.count("Paul"))

myStudents=student1.copy()
print(myStudents) """

""" #Create a list of scores
scores=[90,91,91,90,95,96,80,85,85]

#count how many 90 in the list
print(scores.count(90)) """

""" studentsGroup1=["Sam","Paul","Hnery","Paul","Jack","Paul"]
studentsGroup2=["Frank","Sun","Shelby"]

studentsGroup1.extend(studentsGroup2)
print (studentsGroup1)

print(studentsGroup1.index("Frank"))

#Insert Eric after the first appearence of Sun
studentsGroup1.insert(studentsGroup1.index("Sun")+1,"Eric")
print(studentsGroup1)

#pop the last element of studentsGroup1

print(studentsGroup1.pop())

#Print the list after popping the lest element
print(studentsGroup1)

#print the list after popping a certain position - index
print(studentsGroup1.pop(2))

#Print the list after popping item
print(studentsGroup1)

#remove the first occurance of Paul
print(studentsGroup1.remove("Paul")) """

"""#Write a Python program to sum all the items in a list
#Define a function that will take the list as arguments

 def sum_list(myList):
    #Initialize an accumulator theSum
    sum=0
    #iterate through thr items in myList
    for item in myList:
        #add the item to the sum
        sum += item
    #at the end of the loop the function will return theSum
    return sum

#how to call the function
#declare the list
expense=[100,20,11,55,66,89,283,89]

#call the function
print(sum_list(expense))

#call the list again
score =[90,30,29]
print(sum_list(score))"""

