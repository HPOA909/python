#reference https://www.javatpoint.com/python-tkinter-menu


from tkinter import *
#Toplevel, Button, Tk, Menu  
  
root = Tk()

root.title("Having fun with menubars")
root.geometry('400x400')  

#create a Menu widget
menubar = Menu(root) 

#create the file menu then add commands to it
#note on tearoff 
#By default, the choices in the menu start taking place from position 1.
#If we set the tearoff = 1, then it will start taking place from 0th position.

file = Menu(menubar, tearoff=0)  
file.add_command(label="New")
file.add_command(label="Open")  
file.add_command(label="Save")  
file.add_command(label="Save as...")  
file.add_command(label="Close")  
  
file.add_separator()  
  
file.add_command(label="Exit", command=root.quit)  
 
 #more about add_cascade
 #It is used to create a hierarchical menu to the parent menu by associating the given menu to the parent menu.
menubar.add_cascade(label="File", menu=file)  

#create another m
edit = Menu(menubar, tearoff=0)  
edit.add_command(label="Undo")  

#add a separator
edit.add_separator()  
  
edit.add_command(label="Cut")  
edit.add_command(label="Copy")  
edit.add_command(label="Paste")  
edit.add_command(label="Delete")  
edit.add_command(label="Select All")  
  
menubar.add_cascade(label="Edit", menu=edit) 

help = Menu(menubar, tearoff=0)  
help.add_command(label="About")  
menubar.add_cascade(label="Help", menu=help)  
  
root.config(menu=menubar)  
root.mainloop()  