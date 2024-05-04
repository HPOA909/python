#image Viewer example

#import required libraries
from tkinter import *
from PIL import ImageTk,Image

#path for the images folder
path="C:\\Users\\szaki5\\Desktop\\CISP71_Image_Maninpulation_TextEditor_Tkinter_Examples\\images\\"

root=Tk()
root.title("Image Viewer") #add a title to the window
root.iconbitmap(path+"Boss.ico") #Set the icon for the window


#use ImageTK.PhotoImage and open the required image

my_image1=ImageTk.PhotoImage(Image.open(path+"Occupation_1.png"))
my_label=Label(image=my_image1) #display the image in a label

my_label.pack() #use pack for now to display the image
root.mainloop() #call the mainloop



