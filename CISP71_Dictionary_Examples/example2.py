# Create a dictionary = students
# studentName : studentGrade (key:value)
# students = {"name":grade}

# Create a menu 
# a - Add student
# r - Remove student
# u - Update student
# q - Quit

# On selecting a
# Prompt user to enter student name and grade
# Add item to dictionary

# On selecting r
# Prompt user to enter student name to remove

# On selecting u
# Prompt user to enter student name and new grade to update


students = {}
menuOp = ""

# for i in range(1,6):
#     studentName = input(f"Enter student {i}'s name: ")
#     studentGrade = int(input(f"Enter student {i}'s grade: "))
#     students[studentName] = studentGrade

while menuOp != "q":
    print("\nMENU")
    print("a - Add student")
    print("r - Remove student")
    print("u - Update student")
    print("p - Print unsorted list")
    print("q - Quit")
    print()
    menuOp = input("Enter menu option: ")

    if menuOp == "a":
        studentName = input(f"Enter student name to add: ")
        studentGrade = int(input(f"Enter student grade: "))
        students[studentName] = studentGrade

    elif menuOp == "r":
        studentName = input("Enter student name to remove:")
        del students[studentName]

    elif menuOp == "u":
        studentName = input("Enter student name to update:")
        if studentName in students: 
            studentGrade = int(input("Enter new grade:"))
            students[studentName] = studentGrade
        else:
            print("Add the student first to update their grade.")

    elif menuOp == "p":
        for student, grade in students.items():
            print(f"Student: {student}\tGrade: {grade}")