#Reference https://www.tutorialspoint.com/python/tk_messagebox.htm
#Parameters
#FunctionName − This is the name of the appropriate message box function.
#title − This is the text to be displayed in the title bar of a message box.
#message − This is the text to be displayed as a message.
#options − options are alternative choices that you may use to tailor a standard message box. Some of the options that you can use are default and parent. The default option is used to specify the default button, such as ABORT, RETRY, or IGNORE in the message box. The parent option is used to specify the window on top of which the message box is to be displayed.
#You could use one of the following functions with dialogue box −
# showinfo()
# showwarning()
# showerror ()
# askquestion()
# askokcancel()
# askyesno ()
# askretrycancel ()

from tkinter import *

#import message box in Tkinter
from tkinter import messagebox 

#create our main window
root=Tk()
def hello():
   messagebox.showinfo("Say Hello", "Hello World")

B1 = Button(root, text = "Say Hello", command = hello)
B1.pack()

root.mainloop()