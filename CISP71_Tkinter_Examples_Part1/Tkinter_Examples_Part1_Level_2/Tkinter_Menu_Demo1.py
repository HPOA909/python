#this program will display a menu 
#we will change the font and text of a label
#Reference Safari books online - Python-GUI-Programming-with-Tkinter chapter 6
from tkinter import *

root = Tk()

#declare a variable of string type and set the default value of it to Hi
main_text = StringVar(value='Hi')

#create a Label Widget
label = Label(root, textvariable=main_text)
label.pack()

#create a menu widget
main_menu = Menu(root)
root.config(menu=main_menu)

#Add menu items
main_menu.add('command', label='Quit', command=root.quit)

text_menu = Menu(main_menu, tearoff=False)
text_menu.add_command(label='Set to "Hi"',
                      command=lambda: main_text.set('Hi'))
text_menu.add_command(label='Set to "There"',
                      command=lambda: main_text.set('There'))
main_menu.add_cascade(label="Text", menu=text_menu)

#declare a variable font_bold of boolean type
font_bold = BooleanVar()

#Declare a variable of integer type
font_size = IntVar()

def set_font(*args):
    font_spec = 'TkDefaultFont {size} {bold}'.format(
        size=font_size.get(),
        bold='bold' if font_bold.get() else '')
    label.config(font=font_spec)


font_bold.trace('w', set_font)
font_size.trace('w', set_font)

# appearance menu
appearance_menu = Tk.Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="Appearance", menu=appearance_menu)

# bold text button
appearance_menu.add_checkbutton(label="Bold", variable=font_bold)

# size menu
size_menu = tk.Menu(appearance_menu, tearoff=False)
appearance_menu.add_cascade(label='Font size', menu=size_menu)
for size in range(8, 24, 2):
    size_menu.add_radiobutton(
        label="{} px".format(size),
        value=size, variable=font_size)

root.mainloop()
