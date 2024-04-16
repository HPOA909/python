# Inheritance_Example 2
class MtSAC_Course:
    # TODO: Define constructor with attributes: name, title, desc, units
    #name is like CISD31
    def __init__(self, name, title, desc, units):
        self.name = name
        self.title = title
        self.desc=desc
        self.units=units
 
    # TODO: Define print_info()
    def print_info(self):
        print('Course Information:')
        print('   Course Number:', self.name)
        print('   Course Title:', self.title)
        print('   Course Description:', self.desc)
        print('   Course Units: ', self.units)


class MtSAC_Section(MtSAC_Course):
    # TODO: Define constructor with attributes: 
    #       name, title, desc, units, professor, term, CRN
    def __init__(self, name, title, desc, units, professor, term, CRN):
        MtSAC_Course.__init__(self, name, title, desc, units) 
        self.professor = professor
        self.term = term
        self.CRN = CRN
        

if __name__ == "__main__":
    course_name = input("Enter course name: ")
    course_title = input("Enter course title: ")
    course_desc=input("Enter course description: ")
    course_units=float(input("Enter course number of units: ")) 
    

    section_name =  input("Enter section course name: ")
    section_title =  input("Enter section course title: ")
    section_desc=input("Enter section course description: ")
    section_units=float(input("Enter section course number of units: ")) 
    section_professor = input("Enter section professor: ")
    section_term = input("Enter section term: ")
    section_crn = input("Enter section CRN: ")
    
    my_course = MtSAC_Course(course_name, course_title, course_desc, course_units)
    my_course.print_info()
    
    my_section = MtSAC_Section(section_name, section_title, section_desc, section_units, section_professor, section_term,section_crn)
    my_section.print_info()

    print('   Professor Name:', my_section.professor)
    print('   Term:', my_section.term)
    print('   CRN:', my_section.CRN)