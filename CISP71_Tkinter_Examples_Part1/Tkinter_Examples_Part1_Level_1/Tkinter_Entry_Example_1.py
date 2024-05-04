#This program is going to display to input fields -entry widgets


from tkinter import *

root = Tk()

#create label widgets to display the text beside the input fields and specify the location within the grid
Label(root, text="First Name").grid(row=0)
Label(root, text="Last Name").grid(row=1)

fnameEntry = Entry(root)
lnameEntry= Entry(root)

fnameEntry.grid(row=0, column=1)
lnameEntry.grid(row=1, column=1)

root.mainloop()