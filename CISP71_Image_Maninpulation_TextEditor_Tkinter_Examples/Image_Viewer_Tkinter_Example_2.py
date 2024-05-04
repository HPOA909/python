#reference 
#https://gist.github.com/omiq/da0e69234839ef8e2c0ba528953678f6
#program gets all the images in a folder and the viewer displays the next one on clicking the mouse anywhere in the window
#and displays the full path of the image on the terminal

import os
from PIL import Image
import glob
import tkinter
from PIL import ImageTk


# process the interaction
def event_action(event):
    print(repr(event))
    event.widget.quit()


# clicks
def clicked(event):
    event_action(event)


# keys
def key_press(event):
    event_action(event)


# set up the gui
window = tkinter.Tk()
window.bind("<Button>", clicked)
window.bind("<Key>", key_press)

# get the list of images
path="C:\\Users\\szaki5\\Desktop\\CISP71_Image_Maninpulation_TextEditor_Tkinter_Examples\\images\\"
files = glob.glob(path+"*.jpg")
files += glob.glob(path+"*.png")
files += glob.glob(path+"*.gif")
files.sort(key=os.path.getmtime, reverse=True)

# for each file, display the picture
for file in files:
    print(file)
    window.title(file)
    picture = Image.open(file)
    tk_picture = ImageTk.PhotoImage(picture)
    picture_width = picture.size[0]
    picture_height = picture.size[1]
    window.geometry("{}x{}+100+100".format(picture_width, picture_height))
    image_widget = tkinter.Label(window, image=tk_picture)
    image_widget.place(x=0, y=0, width=picture_width, height=picture_height)

    # wait for events
    window.mainloop()