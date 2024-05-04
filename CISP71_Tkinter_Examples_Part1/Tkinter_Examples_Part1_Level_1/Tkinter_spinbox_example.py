from tkinter import *

root=Tk()

#create a variable of double 
my_double_var = DoubleVar()

#create a spinbox widget

my_spinbox = Spinbox(
    root,
    from_=0.5,
    to=52.0,
    increment=.01,
    textvariable=my_double_var
)
my_spinbox.pack()
root.mainloop()
