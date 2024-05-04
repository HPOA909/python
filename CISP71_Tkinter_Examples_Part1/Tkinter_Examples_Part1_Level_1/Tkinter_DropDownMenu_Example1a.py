#this program is how to use drop down menus in Python and Tkinter
#Reference https://www.delftstack.com/howto/python-tkinter/how-to-create-dropdown-menu-in-tkinter/
##Setting a default itme for the drop down menu and get the selected value using a button
#Binding Dropdown menu
from  tkinter import *

#define a list of options that will be displayed in the dropdown menu- OptionMenu in Tkinter
OptionList = ["Monday",
              "Tuesday",
              "Wednesday",
              "Thursday",
              "Friday"] 

root = Tk()

root.geometry('100x200')
#Drop Down Menus -Option menus
#create an object of OptionMenu
#root--where you are going to place it
#clicked--the variable that will be assigned the value you are going to select
#then specify the items that will show in the option menu

#We need to define the clicked variable. In our case the values Monday, etc. are strings
clicked=StringVar()

#set the default value for the option menu to the first item in the list 
clicked.set(OptionList[0])

#create an OptionMenu widget
#specify parameters
#root-- where it will be placed
#clicked--item selected
#*OptionList--unpack the list you declared
opt=OptionMenu(root,clicked,*OptionList)

#add some configuration to the option menu 
#use config to do that 
#specify the width, font
opt.config(width=90, font=('Helvetica', 12))

#add it to the root using pack and specify the side 
opt.pack(side="top")

#create a label widget that will display your select
#set the text as blank at the beginning
#specify the font and forground color
selectionLabel = Label(text="", font=('Helvetica', 12), fg='red')
selectionLabel.pack(side="top")

#define a function
#recall *args to unpack the args sent to the function
#recall .format() is used to fill in the pockets or place holders
#recall widget.configure is used to update any of the attributes of a widget

def callback(*args):
    selectionLabel.configure(text="The selected item is {}".format(clicked.get()))

#The trace observer has three modes
#observer mode	Explanation
#w	when variable is written by someone
#r	when variable is read by someone
#u	when variable is deleted
#Then clicked.trace("w", callback) means it will call callback function when variable is written or selected by the user.

clicked.trace("w", callback)

root.mainloop()