#Reference https://www.youtube.com/watch?v=mrhccLHtyN4
#Human all human has come set of properties 
#Properties (Name, Gender, Occupation)
#Every human will be doing some kind of common activities called methods
#Methods(Speaks, Do Work, Sleeps)
#self means this class itself
#The __init__ method will be called whenever you create an instance of this class
#an instance has specific values of those properties
#we are going to pass name and occupation as an argument for __init__ method

#let us say that different humans will perform different kind of work
#so if the name of the human is plays tennis his occupation will be tennis ploayer
#this is just to show you how to implement if elif in a method


class Human:
    def __init__(self, n, o):
        self.name = n  #defined a property name for this class
        self.occupation = o #defined a property occupation for this class

#first method
    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name, "plays tennis")
        elif self.occupation == "actor":
            print(self.name, "shoots film")
#second method
    def speaks(self):
        print(self.name, "says how are you?")
#creating an instance of Human class
#when you create an instance of Human class it will first call the __init__ method
tom = Human("tom cruise","actor")

#calling do_work() method for tom object
tom.do_work()
tom.speaks()

#create another instance of the Human class
maria = Human("maria sharapova","tennis player")
maria.do_work()
maria.speaks()