#Reference https://www.delftstack.com/howto/python-tkinter/how-to-change-the-tkinter-label-font-size/
#This example demonstrates how to change the Tkinter label font size.
# We create two buttons Increase and Decrease to increase/decrease the Tkinter label font size.

from tkinter import *

import tkinter.font as tkFont
    
root=Tk()

#add a title to the window
root.title("Buton to Change Label Size!!")

#Specify window size

#create a font style object
fontStyle = tkFont.Font(family="Lucida Grande", size=20)



#define a function that will increase label font
def increase_label_font():
    fontsize = fontStyle['size']
    fontLb['text'] = fontsize+2
    fontStyle.configure(size=fontsize+2)

#define a function that will decrease label font
def decrease_label_font():
    fontsize = fontStyle['size']
    fontLb['text'] = fontsize-2
    fontStyle.configure(size=fontsize-2)
    
#create a button widget   
increaseBt = Button(root, 
                    text="Increase",
                    width=30,
                    command=increase_label_font)

#create another button widget
decreaseBt = Button(root,
                    text="Decrease",
                    width=30,
                    command=decrease_label_font)

#create a label widget

fontLb=Label(root, text="20", font=fontStyle)

#pack the widgets

increaseBt.pack(side=LEFT)
decreaseBt.pack(side=LEFT)
fontLb.pack(side=RIGHT)

#call the  mainloop for tk()
root.mainloop()