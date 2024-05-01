class Pet:
    def __init__(self):
        self.name = ''
        self.age = 0
    
    def print_info(self):
        print(f'Pet Information:')
        print(f'   Name: { self.name }')
        print(f'   Age: { self.age }')

class Cat(Pet):
    def __init__(self):
        Pet.__init__(self) 
        self.breed = ''
        
    def print_info(self):
        Pet.print_info(self)
        print('   Breed: {}'.format(self.breed)) 

my_pet = Pet()
my_cat = Cat()

my_pet.name = input()
my_pet.age = int(input())
my_cat.name = input()
my_cat.age = int(input())
my_cat.breed = input()

my_pet.print_info()
my_cat.print_info()
