#Reference https://www.geeksforgeeks.org/radiobutton-in-tkinter-python/
# Importing Tkinter module 
from tkinter import * 

# Creating root Tkinter window 
root = Tk() 
root.geometry("175x175") 

# Tkinter string variable 
# able to store any string value 
v = StringVar(root, "1") 

# Dictionary to create multiple buttons 
values = {"RadioButton 1" : "1", 
		"RadioButton 2" : "2", 
		"RadioButton 3" : "3", 
		"RadioButton 4" : "4", 
		"RadioButton 5" : "5"} 

# Loop is used to create multiple Radiobuttons 
# rather than creating each button separately 
for (text, value) in values.items(): 
	Radiobutton(root, text = text, variable = v, 
		value = value).pack(side = TOP, ipady = 5) 

# Infinite loop can be terminated by 
# keyboard or mouse interrupt 
# or by any predefined function (destroy()) 
mainloop() 
