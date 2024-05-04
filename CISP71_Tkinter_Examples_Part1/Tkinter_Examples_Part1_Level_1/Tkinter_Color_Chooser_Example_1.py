#colorchooser
# Python program to create color chooser dialog box
from tkinter import *

root=Tk()
from tkinter.colorchooser import askcolor                  
 
def callback():
    result = askcolor(title = "Tkinter Color Chooser")
    label.configure(fg = result[1])
    print(result[1])
     

Button(root, text='Choose Color',command=callback).pack(pady=20)
 
label = Label(root, text = "Color", fg = "black")
label.pack()
 
root.geometry('180x160')
root.mainloop()
