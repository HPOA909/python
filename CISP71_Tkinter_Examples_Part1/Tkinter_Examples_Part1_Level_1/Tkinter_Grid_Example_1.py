#this program will discuss the grid in tkinker
#tkinker grid  https://www.tutorialspoint.com/python/tk_grid.htm
#This geometry manager organizes widgets in a table-like structure in the parent widget.
#more about the display option on the grid http://effbot.org/tkinterbook/grid.htm

#we need to import ImageTk,Image from PIL
#we need to install PIL first
#type 
#pip install Pillow 
#at the command prompt

from tkinter import *

#import message box in Tkinter
from PIL import ImageTk, Image

#create our main window
root=Tk()

#add a title to the window
root.title("Button Displaying Message !!")

# creating fixed geometry of the 
# tkinter window with dimensions 150x200 
root.geometry('300x300')

#create two label widgets and add them to the grid 
heightLb=Label(root, text="Height")
widthLb=Label(root, text="Width")

#create two entry widgets and add them to the grid
heightEn=Entry(root)
widthEn=Entry(root)

#declare a variable
CheckVar1 = IntVar()

#create a checkbutton widget
aspectCb= Checkbutton(root, text = "Reserve", variable = CheckVar1, 
                 onvalue = 1, offvalue = 0, )

#create an image widget
path="C:/Users/szaki5/Desktop/CISP71_Tkinter_Examples_Part1/Tkinter_Examples_Part1_Level_1/icons/Superman-icon.png"
src_img= PhotoImage(file=path)
img = Label(root, image = src_img)

#create two button widgets
zoomInBt=Button(root,text='Zoom In')
zoomOutBt=Button(root,text='Zoom Out')

#add the widgets to the grid proper locations
heightLb.grid(row=0,sticky=E)
widthLb.grid(row=1,sticky=E)
heightEn.grid(row=0, column=1)
widthEn.grid(row=1, column=1)
aspectCb.grid(columnspan=2, sticky=W)
#you need to include the image on a label to be able to display it in a grid
img.grid(row=0, column=2, columnspan=2, rowspan=2,
               sticky=W+E+N+S, padx=5, pady=5)
zoomInBt.grid(row=2,column=2)
zoomOutBt.grid(row=2,column=3)


root.mainloop()