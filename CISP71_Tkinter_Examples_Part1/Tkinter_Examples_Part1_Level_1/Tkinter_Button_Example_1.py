#this example will show how to display a messagebox on clicking a button
#more about button configuration https://www.tutorialspoint.com/python/tk_button.htm

from tkinter import *

#import message box in Tkinter
from tkinter import messagebox 

#create our main window
root=Tk()

#add a title to the window
root.title("Button Displaying Message !!")

# creating fixed geometry of the 
# tkinter window with dimensions 150x200 
root.geometry('300x300') 


#define a function that will take care of the click event
def displayMessage():
   messagebox.showinfo( "Hello Python", "Hello World")
   
#create a button widget
#will go on root has text and specify the command

messageBt = Button(root, text ="Hello", command = displayMessage)

#other button attributes to try
#specify forground color
# messageBt = Button(root, 
#                    text ="Hello",
#                    fg="blue",
#                    command = displayMessage)


#**relief** Relief specifies the type of the border. Some of the values are sunkne, raised, groove, and ridge.
# messageBt = Button(root, 
#                    text ="Hello",
#                    fg="blue",
#                    width=40,
#                    relief="groove",
#                    command = displayMessage)



#pack the widgets
messageBt.pack()

#call the mainloop of Tk()
root.mainloop()