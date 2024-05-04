#https://tkdocs.com/
#https://docs.python.org/3/library/tk.html
#reference the video play list
#https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

#import tkinter
#tkinter is a built in python so we want to import everything
#Evertyhing in tkinter is a widget (button, textboxes, etc.) 
#first thing you create is the root widget

from tkinter import *

#Toplevel widget of Tk which represents mostly the main window of an application.


root=Tk()

#we will create a label widget
#to create anything is in kinter is really a two-step process
# you have to define the thing and create it and then you have to put it up on the screen

#create a label widget
myLabel=Label(root, text="Welcome to Python Course")

#we want this to go into our root widget
#There are many way to put things on the window in tkinter
#One way is pack. you're just shoving it in there at the first available spot right it's just
#sort of it'll be the size that it is.
myLabel.pack()


#now the last thing we need to do is create an event loop
# and what an event loop is when you have a graphical user interface when you have a program
#running it's always looping constantly and that's how it figures out what's going on so as it's looping you might
#move your mouse cursor right since it's looping it notices all the mouse is here now it's here now it's here now it's
#here because it's continually looping if you go to click a button you know it loops sees you moving towards that
#button as its looping looping looping so it's a constant loop 

root.mainloop()
