#we are going to add a button and define a function to take care of the click event
#this example is going to display two buttons
#on clicking the first one the system will quit
#on clicking the second one the text on a label will change

from tkinter import *

root=Tk()

#add a title to the window
root.title("More fun with tkinter buttons")

# creating fixed geometry of the 
# tkinter window with dimensions 150x200 
root.geometry('300x300') 

#define a function that will update the text displayed on greatingLb
#recall you can update the text of the label in several ways
#greatingLb['text']= 'xxx' where xxx is the new text
#or
#greatingLb.configure(text='xxx') where xxx is the new text

def greating():
    greatingLb.configure(text="Hello welcome to Super Python Course")
  
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
                   command=greating)

#create a label widget 
greatingLb=Label(root, text='')



#pack the widgets on the root specify the side if required 
frame.pack()
quitBt.pack(side=LEFT)
displayBt.pack(side=LEFT)
greatingLb.pack()

#Call the mainloop of Tk
root.mainloop()