""" students={
    "name" : "Sam",
    "age" : 20,
    "major" : "Networking",
}
print(students)
 """
""" #accessing the names of students
print("Student name:",students["name"])
print (students["age"])

#using the get object
print(students.get("major"))

#retrieve all the keys
print(students.keys())

print(students.items())

#retrieve the values
print(students.values())

#clear all items in the dict
print(students.clear()) """

""" #modify a value for the key 
students["major"]="Programming"

print(students.get("major"))

students["age"]=25

print(students.get("age"))

#print the keys of the dict by iteration
for student in students:
    print(student)

for student in students:
    print(students[student])

print("Key \t Value")
for astudent in students:
    print(astudent,"\t",students[astudent])

#use items method of the dict to print
print("Key \t Value")
for key,value in students.items():
    print(key, "\t", value)

print(len(students)) """

""" students["GPA"]=1.0

print(students)

students.pop("GPA")
print(students)

newStudent=students.copy()
print(newStudent)

newStudent=students
print(newStudent)

students.update({"age":24,"name":"Henry"})
print(students) """

""" d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)
 """

"""  #8.18 LAB: Middle item
#   Given a sorted list of integers, output the middle integer. Assume the number of integers is always odd.
#   Ex: If the input is:
#   2 3 4 8 11
#   the output is:
#   4
#   The maximum number of inputs for any test case should not exceed 9. If exceeded, output "Too many inputs".
#   Ex: If the input is:
#   10 20 30 40 50 60 70 80 90 100 110
#   The output is 
#   Too many inputs
#Hint: First read the data into a list. Then, based on the list's size, find the middle item.

num=input()

splice=num.split()
data= [int(values) for values in splice]

valuesNum= len(data)
if valuesNum > 9:
    print("Too many inputs")
else:
    medium = valuesNum // 2
    print(data[medium]) """

""" #create a dictionary students 
#studentName and grade
#students={'name':'sam', 'grade':90}
#create a menu 
#a  to add a student
#r to remove a student
#u to update a student
#q to quit

#on selecting a 
#the user will be prompted to enter the student name and grade 
#then you need to add this item to the dictionary
# on selecting r 
#the user will be prompted to enter the student name to remove from the dictionary
#on selecting u
#the user will be prompted to enter student name and new student grade


#create a dictionary that contains students
#studentName as the keys, student grades as the values
#create a menu
#a: Add a student
#r: Remove a student
#u: Update a student
#q: Quit Program

initiation =Enter your input:
a: Add a student
r: Remove a student
u: Update a student
q: Rage quit

students={}
program = ''
while program != 'q':
    program = input(initiation)

    if program == 'a':
        name = input("Enter a name: ")
        grade = int(input("Enter a grade: "))
        students[name]=grade
    elif program == 'r':
         """



#Smaple submitted by a student 
#create dictionary students
students = {}
#studentName and grade with the format students = {name: sam, grade: 90}
for i in range(5):
    name = input("Enter student {} name: ".format(i+1))
    grade = int(input("Enter student {} score: ".format(i+1)))
    students[name] = grade
list_students = sorted(list(students.keys()))

#create menu
selection = ""
while selection != 'q':
    print("\n=====STUDENT MENU=====")
    print('a - Add student')
    print('r - Remove student')
    print('u - Update student info')
    print('p - Print the students')
    print('q - Quit the program')
    selection = input("Enter a menu option: ")

    if selection == 'a':
        name = input("Enter student name: ")
        grade = int(input("Enter student score: "))
        students[name] = grade
    elif selection == 'r':
        name = input("Enter student name to be removed: ")
        del students[name]
    elif selection == 'p':
        list_students = sorted(list(students.keys()))
        print("Student Roster")
        for i in list_students:
            print("Name: {}| Grade: {}" .format(i,students[i]))
    elif selection == 'u':
        name = input("Enter student name: ")
        grade = int(input("Enter new student score: "))
        students[name] = grade
    elif selection == 'q':
        print("You have terminated the program.")