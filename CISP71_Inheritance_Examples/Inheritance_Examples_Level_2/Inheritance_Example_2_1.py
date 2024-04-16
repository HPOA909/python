#The base class person has attributes name and age. The derived class student inherits attributes from the base class person class and includes a major attribute. Complete the program to:
# Create a generic person, and print the person's information using print_info().
# Create a student person, use print_info() to print the student's information, and add a statement to print the student's major attribute.
#example 2 similar to one of your labs
class Person:
    def __init__(self):
        self.name = ''
        self.age = 0

    def print_info(self):
        print('person Information:')
        print('   Name:', self.name)
        print('   Age:', self.age)

class Student(Person):
    def __init__(self):
        Person.__init__(self) 
        self.Major = ''

my_person = Person()
my_student = Student()

person_name = input("Person Name: ")
person_age = int(input("Person Age: "))
student_name = input("Student Name: ")
student_age = int(input("Student Age: "))
student_major = input("Student Major: ")

# TODO: Create generic person (using person_name, person_age) and then call print_info()
my_person.name = person_name
my_person.age = person_age
my_person.print_info()

# TODO: Create student person (using student_name, student_age, student_major) and then call print_info()
my_student.name = student_name
my_student.age = student_age
my_student.major = student_major
my_student.print_info()

# TODO: Use my_student.major to output the major of the student
print('   major:', my_student.major)