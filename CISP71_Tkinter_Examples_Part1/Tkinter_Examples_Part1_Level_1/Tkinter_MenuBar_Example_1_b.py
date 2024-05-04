#reference https://www.javatpoint.com/python-tkinter-menu


from tkinter import *
#Toplevel, Button, Tk, Menu  
  
root = Tk()

root.title("Having fun with menubars")
root.geometry('400x400')  

#create a Menu widget
menubar = Menu(root) 

#create a menu item and it will be located at the menubar
file = Menu(menubar, tearoff=0) 

#add menu sub items of file menu item
file.add_command(label="New")
file.add_command(label="Open")  
file.add_command(label="Save")  
file.add_command(label="Save as...")  
file.add_command(label="Close")  
  
file.add_separator()  
  
file.add_command(label="Exit", command=root.quit)  

 #more about add_cascade
 #It is used to create a hierarchical menu to the parent menu by associating the given menu to the parent menu.
 #add the file menu item to the menu bar and give it a label File
menubar.add_cascade(label="File", menu=file)  

#create another menu item edit
edit = Menu(menubar, tearoff=0)  
#add it to the menubar with a label Edit 
menubar.add_cascade(label="Edit", menu=edit) 

#create a menu item help that will be located at menubar
help = Menu(menubar, tearoff=0)  

#add this menu item to menubar and it is a label type Help
menubar.add_cascade(label="Help", menu=help)  
 
 #configure our window root that the menu will be menubar widget that we created 
root.config(menu=menubar)

#call mainloop of Tk()  
root.mainloop()  