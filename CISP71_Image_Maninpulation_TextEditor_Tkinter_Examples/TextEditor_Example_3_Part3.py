#text editor
#we are going to implement open new save and save as functions

from tkinter import *
from tkinter import filedialog #importing filedialog
from tkinter import font #importing font

root=Tk() #our window
root.title('Having fun with text editor') #adding a title for the window
path='C:/Users/szaki5/Desktop/CISP71_Image_Maninpulation_TextEditor_Tkinter_Examples/icons/'
root.iconbitmap(path+'boss.ico') #assigning the icon for the window
root.geometry("1200x660") #setting the geometry of the window

#Create a new file function
def new_file():
    my_text.delete("1.0", END) #clear the text
    root.title('New File - Still Fun') # change the window title
    status_bar.config(text="New File       ") #change the text of the status bar
    
#Create open file function
def open_file():
    my_text.delete("1.0", END) #clear the text
    root.title('Update File - Still Fun') # change the window title
    #grab file name
    path="C:/Users/szaki5/Desktop/CISP71_Image_Maninpulation_TextEditor_Tkinter_Examples/data/"
    #use the file dialog
    text_file=filedialog.askopenfilename(initialdir=path,
                                         title="Open File",
                                         filetypes=(("Text Files","*.txt"),
                                                    ("Python Files","*.py"),
                                                    ("All files","*.*")))
    name=text_file #save the file name
    status_bar.config(text=name) #display the file name in the status bar
    #Open the file
    text_file=open(text_file,'r') #open the file in read mode
    content=text_file.read() #read everything in the file and assign it to content
    my_text.insert(END,content) #insert the content into the textbox
    text_file.close() #close the opened file
    
#Create a function save as file
def save_as_file():
    text_file=filedialog.asksaveasfilename(defaultextension=".*",
                                           initialdir=path,
                                           title="Save File",
                                            filetypes=(("Text Files","*.txt"),
                                                    ("Python Files","*.py"),
                                                    ("All files","*.*")))
    #if we picked a file name we want to do some steps
    if text_file:
        name=text_file
        status_bar.config(text=name+' saved')#update status bar
        #save the file
        text_file=open(text_file,'w') #open the file in write mode
        text_file.write(my_text.get(1.0,END)) #get everything in your text box
        text_file.close() #close the file
        

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

my_menu=Menu(root) #Create Menu
root.config(menu=my_menu) #configure the menu for the root

#Add File Menu
#note tearoff = False to get rid of the dotted line 
#that shows that on clicking it take the menu and tear it off
file_menu=Menu(my_menu, tearoff=False) #create a file menu
my_menu.add_cascade(label="File", menu=file_menu) #Add hierarchical menu item.
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save")
file_menu.add_command(label="Save AS", command=save_as_file)
file_menu.add_separator() #add a separator
file_menu.add_command(label="Exit", command=root.quit)

#Add Edit Menu
edit_menu=Menu(my_menu,tearoff=False) #create a file menu
my_menu.add_cascade(label="Edit", menu=edit_menu) #Add hierarchical menu item.
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

#Add Status Bar To Bottom of App. It will be a label
#anchor east to put it in the right corner
#ipady=5 internal padding
status_bar=Label(root, text="Ready     ", anchor=E) 
status_bar.pack(fill=X, side=BOTTOM, ipady=5) # pack it and give it a fill of x to stretch it
root.mainloop() #call the mainloop()



