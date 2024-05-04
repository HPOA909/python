#this program is how to use drop down menus in Python and Tkinter
#Reference https://www.youtube.com/watch?v=3E_fK5hCUnI&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=18
from tkinter import *

root=Tk()
#add a title to your root
root.title("Having Fun With Drop Down Menus")

#specify the size of the window
root.geometry("400x400")

#Drop Down Menus -Option menus
#create an object of OptionMenu
#root--where you are going to place it
#clicked--the variable that will be assigned the value you are going to select
#then specify the items that will show in the option menu

#We need to define the clicked variable. In our case the values Monday, etc. are strings
clicked=StringVar()

drop = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"  )
#add it to the root just using pack for now

drop.pack()

#start the looping process for the root
#Call the main loop of TK
root.mainloop()
