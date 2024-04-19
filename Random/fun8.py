""" #Create a class student and create object of that class
class Student:
    pass
#create an instance of this class
student1=Student()
student2=Student()
#assign values to the attribute

student1.first="Sam" """

""" class Student:
    num_of_students=0
    enrollmentFees=45

    def __init__ (self, first, last, gpa):
        self.first = first
        self.last = last
        self.gpa = gpa
        self.email = first+'.'+last+"@gmail.com"
        Student.num_of_students += 1

    def rosterName (self):
        return '{} {}'.format(self.last, self.first)

    def enrollment (self):
        return '{} enrollment fees'.format(Student.enrollmentFees)

student1=Student("Sam", "Mark", 8.0)
student2=Student("Shelby", "Howard", 9.9) """

""" class Customer :
    customerCount = 0

    def __init__ (self, name, accountNumber, balance):
        self.name = name
        self.accountNumber = accountNumber
        self.balance = balance
        Customer.customerCount += 1

    def displayCount(self):
        print ("Total number of customers: %d "%Customer.customerCount)

    def displayCustomer (self):
        print("Customer Info:")
        print("Name: ", self.name, "Account Number ",self.accountNumber) """

""" #using instranciation to create a variable using the student class

class Student:
    num_of_students=0 #Class variable
    def __init__ (self):
        self.name=''
        self.gpa=0
        #Increment the number of students
        Student.num_of_students += 1
#First instance
student1=Student()
print("First Step")
print(student1.name)
print(student1.gpa)

#Second instance
student2=Student()
#Update and modify all the attribute
student1.name="Sam"
student1.gpa=4.0

print("Second Step")
print(student1.name)
print(student1.gpa)

student2.name="Michael"
student2.gpa=4.0

print (student2.name)
print(student2.gpa)
print("Number of students:", Student.num_of_students) """

""" class Car:
    def __init__(self):
        self.model_year = 0
        # TODO: Declare purchase_price attribute
        self.purchase_price = 0
        self.current_value = 0

    def calc_current_value(self, current_year):
        depreciation_rate = 0.15
        # Car depreciation formula
        car_age = current_year - self.model_year
        self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age)
    
    # TODO: Define print_info() method to output model_year, purchase_price, and current_value
    def print_info(self):
        print("Car\'s information:")
        print('Model year: {}'.format(self.model_year))
        print ('Purchase price: {}'.format(self.purchase_price))
        print ('Current value: {}'.format(self.current_value))

if __name__ == "__main__":    
    year = int(input('Enter the year: ')) 
    price = int(input('Enter the price: '))
    current_year = int(input('Enter the current year: '))
    
    my_car = Car()
    my_car.model_year = year
    my_car.purchase_price = price
    my_car.calc_current_value(current_year)
    my_car.print_info()
     """

""" class Artist:
    # TODO: Define constructor with parameters to initialize instance attributes
    #       (name, birth_year, death_year)
    def __init__ (self,name='',birth_year=0,death_year=0):
        self.name=name
        self.birth_year=birth_year
        self.death_year=death_year

    # TODO: Define print_info() method
    def print_info(self):
        if self.death_year == -1:
            print('Artist: {} , born: {}'.format(self.name,self.birth_year))
        else:
            print('Artist: {} , born: {} , died: {}'.format(self.name,self.birth_year,self.death_year))
      
class Artwork:
    # TODO: Define constructor with parameters to initialize instance attributes
    #       (title, year_created, artist)
    def __init__ (self,title='None',year_created=0,artist=Artist()):
        self.title=title
        self.year_created=year_created
        self.artist=artist

    # TODO: Define print_info() method
    def print_info(self):
        self.artist.print_info()
        print('title: {}, {}'.format(self.title,self.year_created))

if __name__ == "__main__":
    user_artist_name = input('Enter artist name: ')
    user_birth_year = int(input('Enter artist birth year: '))
    user_death_year = int(input('Enter artist death year; enter -1 if alive: '))
    user_title = input('Enter title: ')
    user_year_created = int(input('Enter the year created: '))

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    new_artwork = Artwork(user_title, user_year_created, user_artist)
  
    new_artwork.print_info() """

class Triangle:   
    def __init__(self):
        self.base = 0
        self.height = 0

    def set_base(self, user_base):
        self.base = user_base

    def set_height(self, user_height):
        self.height = user_height
   
    def get_area(self):
        area = 0.5 * self.base * self.height
        return area
   
    def print_info(self):
        print(f'Base: {self.base:.2f}')
        print(f'Height: {self.height:.2f}')
        print(f'Area: {self.get_area():.2f}')

if __name__ == "__main__":
    triangle1 = Triangle()
    triangle2 = Triangle()

    # TODO: Read and set base and height for triangle1 (use set_base() and set_height())
    user_base=float(input('Base: '))
    user_height=float(input("Height: "))
    triangle1.set_base(user_base)
    triangle1.set_height(user_height)

    # TODO: Read and set base and height for triangle2 (use set_base() and set_height())
    user_base=float(input('Base: '))
    user_height=float(input("Height: "))
    triangle2.set_base(user_base)
    triangle2.set_height(user_height)
      
    print('Triangle with smaller area:')  
    
    # TODO: Determine smaller triangle (use get_area())
    #       and output smaller triangle's info (use print_info())
    if triangle1.get_area() < triangle2.get_area():
        triangle1.print_info
    else:
        triangle2.print_info