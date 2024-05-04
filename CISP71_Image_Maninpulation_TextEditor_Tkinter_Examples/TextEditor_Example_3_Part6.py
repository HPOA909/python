#text editor part 6
#create a simple toolbar 
#we are going to change text to bold and italic

from tkinter import *
from tkinter import filedialog #importing filedialog
from tkinter import font #importing font

root=Tk() #our window
root.title('Having fun with text editor') #adding a title for the window
path='C:/Users/szaki5/Desktop/CISP71_Image_Maninpulation_TextEditor_Tkinter_Examples/icons/'
root.iconbitmap(path+'boss.ico') #assigning the icon for the window
root.geometry("1200x660") #setting the geometry of the window

#global variables added
global open_status_name #set variable for open file name
open_status_name=False

global selected
selected=False

################################
#########functions section######
################################ 
       
#Create a new file function
def new_file():
    my_text.delete("1.0", END) #clear the text
    root.title('New File - Still Fun') # change the window title
    status_bar.config(text="New File       ") #change the text of the status bar
    #added to fix save file
    global open_status_name #set variable for open file name
    open_status_name=False
   
   
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
    #steps we need for the save_file function later to save the file name globally
    #if you hit cancel you have no file name to save globally
    #check if there is a file name
    if text_file:
        global open_status_name #make file name global
        open_status_name=text_file
    
    name=text_file #save the file name
    status_bar.config(text=name) #display the file name in the status bar
    #Open the file
    text_file=open(text_file,'r') #open the file in read mode
    content=text_file.read() #read everything in the file and assign it to content
    my_text.insert(END,content) #insert the content into the textbox
    text_file.close() #close the opened file

#Create a function save_as file
def save_as_file():
    path="C:/Users/szaki5/Desktop/CISP71_Image_Maninpulation_TextEditor_Tkinter_Examples/data/"
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
        
#create a function save_file 
def save_file():
    global open_status_name #declare again may be we will change it
    if open_status_name: #check if the file already opened
        text_file=open(open_status_name,'w') #open the file in write mode
        text_file.write(my_text.get(1.0,END)) #get everything in your text box
        text_file.close() #close the file
        status_bar.config(text=open_status_name+' saved')
    else: #if the file is not already opened and it is a new one we need save as
        save_as_file() 
        
#create a function copy_text 
#we need to pass something
def copy_text(e):
    global selected
    if my_text.selection_get():
        selected=my_text.selection_get()

        
#create a function cut_text
def cut_text(e):
    global selected
    if my_text.selection_get(): #if something is highlighted we want to do something with it
        selected=my_text.selection_get() #grab selected text from text box
        my_text.delete("sel.first","sel.last") #delete selected text from text box
        
        



#create a function paste_text
def paste_text(e):
    if selected: #check is any text is selected
        #we need to know where to paste, usually it is where the cursor is positioned
        position=my_text.index(INSERT) #grabs whever our cursor is sitting in our text box
        #we will use that to insert whatever we have cut
        my_text.insert(position,selected)


#*** create  bold-it function Bold text
def bold_it():
    #create our font
    bold_font=font.Font(my_text, my_text.cget("font"))
    #configure this font set the weight to bold
    bold_font.configure(weight="bold")
    #configure a tag
    my_text.tag_configure("bold",font=bold_font)
    #define current tags
    current_tags=my_text.tag_names("sel.first")
    #if statement to see if tag has been set
    if "bold" in current_tags:
        my_text.tag_remove("bold","sel.first", "sel.last")
    else:
        my_text.tag_add("bold","sel.first", "sel.last")
#** create italics-it function
def italics_it():
     #create our font
    italics_font=font.Font(my_text, my_text.cget("font"))
    #configure this font set the weight to bold
    italics_font.configure(slant="italic")
    #configure a tag
    my_text.tag_configure("italic",font=italics_font)
    #define current tags
    current_tags=my_text.tag_names("sel.first")
    #if statement to see if tag has been set
    if "italic" in current_tags:
        my_text.tag_remove("italic","sel.first", "sel.last")
    else:
        my_text.tag_add("italic","sel.first", "sel.last")

    

#####################
### Tool bar       ##
#####################
#*** Create a toolbar frame
toolbar_frame=Frame(root)
toolbar_frame.pack(fill=X)



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
################################
####      Menu             #####
################################
my_menu=Menu(root) #Create Menu
root.config(menu=my_menu) #configure the menu for the root

#Add File Menu
#note tearoff = False to get rid of the dotted line 
#that shows that on clicking it take the menu and tear it off
file_menu=Menu(my_menu, tearoff=False) #create a file menu
my_menu.add_cascade(label="File", menu=file_menu) #Add hierarchical menu item.
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command = save_file)
file_menu.add_command(label="Save AS", command=save_as_file)
file_menu.add_separator() #add a separator
file_menu.add_command(label="Exit", command=root.quit)

#Add Edit Menu
edit_menu=Menu(my_menu,tearoff=False) #create a file menu
my_menu.add_cascade(label="Edit", menu=edit_menu) #Add hierarchical menu item.
#we are going to use lambda we pass 1 we are not actually passing anything here
#we will deal with event we will pass an event so that we can
#later we can add short cut keys
edit_menu.add_command(label="Cut", command=lambda: cut_text(1))
edit_menu.add_command(label="Copy", command=lambda: copy_text(1))
edit_menu.add_command(label="Paste", command=lambda: paste_text(1))
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

################################
#####   Status bar         #####
################################

#Add Status Bar To Bottom of App. It will be a label
#anchor east to put it in the right corner
#ipady=5 internal padding
status_bar=Label(root, text="Ready     ", anchor=E) 
status_bar.pack(fill=X, side=BOTTOM, ipady=5) # pack it and give it a fill of x to stretch it

####################
##****** Buttons for the toolbar###
bold_button=Button(toolbar_frame,text="Bold", command=bold_it)
bold_button.grid(row=0,column=0,sticky=W, padx=5)

italics_button=Button(toolbar_frame,text="Italics", command=italics_it)
italics_button.grid(row=0,column=1, padx=5)


root.mainloop() #call the mainloop()



