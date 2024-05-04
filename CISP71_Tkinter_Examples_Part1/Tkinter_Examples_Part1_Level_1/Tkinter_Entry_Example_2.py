#This program is going to display to input fields -entry widgets
#we have two buttons one to quit and the other to display the entry widget contents on the terminal
#reference https://www.python-course.eu/tkinter_entry_widgets.php


from tkinter import *

root = Tk()
import tkinter as tk

#define a funtion to show the entry fields
#recall you can use the get method to get what the user entered in the entry widget

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (fnameEn.get(), lnameEn.get()))

#create label widget and add it to the grid on the first row
Label(root, 
         text="First Name").grid(row=0)

#create a label widget and add it to the grid on the second row
Label(root, 
         text="Last Name").grid(row=1)

#create entry widgets 

fnameEn = Entry(root)
lnameEn = Entry(root)

#specify where on the grid you are going to add those entry widgets
fnameEn.grid(row=0, column=1)
lnameEn.grid(row=1, column=1)

#create button widget and specify where it will go, text displayed on it and command that will run on clicking the button
#then specify the location of the grid it will be displayed on which row and which column the pading
#more about tkinter grid #https://www.tutorialspoint.com/python/tk_grid.htm

Button(root, 
          text='Quit', 
          command=root.quit).grid(row=3, 
                                    column=0, 
                                    sticky=W, 
                                    pady=4)
          
#create another button widget
Button(root, 
          text='Show', command=show_entry_fields).grid(row=3, 
                                                       column=1, 
                                                       sticky=W, 
                                                       pady=4)


#notice we are not using pack we are using the grid this time
root.mainloop()