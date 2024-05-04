#text editor
from tkinter import *
from tkinter import filedialog #importing filedialog
from tkinter import font #importing font

root=Tk() #our window
root.title('Having fun with text editor') #adding a title for the window
path='C:/Users/szaki5/Desktop/CISP71_Image_Maninpulation_TextEditor_Tkinter_Examples/icons/'
root.iconbitmap(path+'boss.ico') #assigning the icon for the window
root.geometry("1200x660") #setting the geometry of the window

my_frame=Frame(root) #create a frame widget that will exist on root
my_frame.pack(pady=5) # place the frame we will use pack for now padding 5 pixels 

text_scroll =Scrollbar(my_frame) #create our scroll bar for the text box
text_scroll.pack(side=RIGHT, fill=Y) #put it on the right side and the fill is y axis


#create a text widget that will be placed on my_frame
#specify width, height and font
#specify the background color of selected text to yellow
#specigy the forground color of the selected or hightlight text to black
#we want to undo stuff
#let set the yscroll -we are going to specify the text_scroll scroll bar
my_text=Text(my_frame, width=97, height=25,
             font=("Helvetica",16),
             selectbackground="yellow",
             selectforeground="black",
             undo=True, yscrollcommand=text_scroll.set)


text_scroll.config(command=my_text.yview) #configure the Scrollbar
my_text.pack()









root.mainloop() #call the mainloop()



