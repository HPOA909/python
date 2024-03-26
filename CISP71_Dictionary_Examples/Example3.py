
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