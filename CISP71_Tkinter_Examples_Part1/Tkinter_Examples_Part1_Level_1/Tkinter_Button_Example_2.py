#we are going to add a button and define a function to take care of the click event
#this example is going to display two buttons
#on clicking the first one the system will quit
#on clicking the second one a message will be displayed on the terminal

from tkinter import *

root=Tk()

#define a function that will take display the message on the terminal
def write():
    print("Tkinter is easy to use!")
  
#create a frame widget
frame=Frame(root)

#create a button widget specify where it will go on frame
#specify the text and foreground color
#specify the command or action on clicking the button 
#Note if you typed the command=quit then it will run the quit built in method in python
quitBt = Button(frame, 
                   text="QUIT", 
                   fg="red",
                  command=quit)
#create another button to display a message on the terminal
#specify command to call the function write that you just created
displayBt = Button(frame,
                   text="Hello",
                   command=write)



#pack the widgets on the root specify the side if required 
frame.pack()
quitBt.pack(side=LEFT)
displayBt.pack(side=LEFT)

#Call the mainloop of Tk
root.mainloop()