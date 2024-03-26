#create a dictionary students 
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

prompt = '''Enter an input:
a: Add a student
r: Remove a student
u: Update a student
q: Quit Program
'''

students = {}
program_input = ''
while program_input != 'q':
    program_input = input(prompt)

    if program_input == 'a':
        name = input('Enter a name: ')
        grade = int(input('Enter a grade: '))
        students[name] = grade
    
    if program_input =='r':
        name = input('Enter a name to remove: ')
        del(students[name])
    
    if program_input == 'u':
        name = input('Enter a name to change grade: ')
        grade = int(input('Enter new grade: '))
        students[name] = grade
print(students)