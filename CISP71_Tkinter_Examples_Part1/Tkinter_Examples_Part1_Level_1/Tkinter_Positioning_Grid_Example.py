#Reference https://www.youtube.com/watch?v=BSfbjrqIw20&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=2
#we are going to use the grid system to position things on the screen
from tkinter import *
root=Tk()
#creating a label widget
myLabel1=Label(root, text="Hello, Welcome to Python course!!! ")
myLabel2=Label(root, text="I am sure you will enjoy this course. ")

#We are going to use the grid
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1, column=0)


root.mainloop()