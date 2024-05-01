class Course:
    # TODO: Define constructor with attributes
    def __init__(self, number, title):
        self.course_number=number
        self.course_title=title

    # TODO: Define print_info()
    def print_info(self):
        print('Course Information:')
        print(f'   Course Number: {self.course_number}')
        print(f'   Course Title: {self.course_title}')

class OfferedCourse(Course):
    # TODO: Define constructor with attributes
    def __init__(self, course_number,course_title,instructor_name,location,class_time):
        self.course_number=course_number
        self.course_title=course_title
        self.instructor_name=instructor_name
        self.location=location
        self.class_time=class_time

    def print_info(self):
        print('Course Information:')
        print(f'   Course Number: {self.course_number}')
        print(f'   Course Title: {self.course_title}')
        print(f'   Instructor Name: {self.instructor_name}')
        print(f'   Location: {self.location}')
        print(f'   Class Time: {self.class_time}')

if __name__ == "__main__":
    course_number = input()
    course_title = input()

    o_course_number =  input()
    o_course_title =  input()
    instructor_name = input()
    location = input()
    class_time = input()
    
    my_course = Course(course_number, course_title)
    my_course.print_info()
    
    my_offered_course = OfferedCourse(o_course_number, o_course_title, instructor_name, location, class_time)
    my_offered_course.print_info()
