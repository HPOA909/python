
#Python #GUI #filedialog #tkinter #open #file #tutorial #beginners

from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\szaki5\\Desktop\\CISP71_Image_Maninpulation_TextEditor_Tkinter_Examples\\",
                                          title="Open file okay?",
                                          filetypes= (("text files","*.txt"),
                                          ("all files","*.*")))
    file = open(filepath,'r')
    print(file.read())
    file.close()

window = Tk()
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()