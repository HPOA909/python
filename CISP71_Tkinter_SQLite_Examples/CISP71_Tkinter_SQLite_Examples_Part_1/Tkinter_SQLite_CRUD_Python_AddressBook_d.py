#use sqlite with python
#This program is going to create a form to insert and show records of the address book sqlite table that we just created
#reference https://www.sourcecodester.com/tutorials/python/13645/python-display-sqlite3-data-treeview.html
#Display all the records from addressbook in a TreeView

from tkinter import*
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

from PIL import ImageTk,Image
#sqlite is built in Python

import sqlite3

#create the main window
root=Tk()
#give the window a title
root.title("Having fun with sqlite")

#declare a variable to save the path of the icon file
#Recall we use the forward slash instead of backward slash

#change the size of the window
root.geometry("300x300")
#declare a variable to save the path of the icon file
#Recall we use the forward slash instead of backward slash

path="C:/Users/szaki5/Desktop/CISP71_Tkinter_SQLite_Examples/CISP71_Tkinter_SQLite_Examples_Part_1/"
#changing the icon of the window
root.iconbitmap(path+"icons/Boss.ico")

conn=sqlite3.connect(path+"address_book.db")
#==================================METHODS============================================
    
def populateView():
    #connect to database
    #oid primary key
    #fetchall retrieves all records
    #fetchmany(50)
    #fetchone
    #records is a list of tuples inside it
    conn=sqlite3.connect(path+"address_book.db")
    tree.delete(*tree.get_children())
    try:
        c=conn.cursor()
        c.execute("select *,oid from contacts")
        records=c.fetchall()
        
        for record in records:
           tree.insert('', 'end', values=(record[0], record[1], record[2]))
        
        #commit changes
        conn.commit()
        #close connection
        conn.close()
                 
    except:
         print("error in operation")
         conn.rollback()
    conn.close()
#==================================FRAME==============================================
# Top = Frame(root, width=700, height=50, bd=8, relief="raise")
# Top.pack(side=TOP)
Button_Group=Frame(root, width=700, height=50)
Button_Group.pack(side=TOP)
Buttons = Frame(Button_Group, width=200, height=50)
Buttons.pack(side=LEFT)
# Buttons1 = Frame(Button_Group, width=500, height=50)
# Buttons1.pack(side=RIGHT)
Body = Frame(root, width=700, height=300, bd=8, relief="raise")
Body.pack(side=BOTTOM)


#==================================LABEL WIDGET=======================================
# txt_title = Label(Top, width=300, font=('arial', 24), text = "Python - Display SQLite3 Data In TreeView")
# txt_title.pack()

#==================================BUTTONS WIDGET=====================================
btn_display = Button(Buttons, width=15, text="Display All", command=populateView)
btn_display.pack(side=LEFT)


#==================================LIST WIDGET========================================
scrollbary = Scrollbar(Body, orient=VERTICAL)
scrollbarx = Scrollbar(Body, orient=HORIZONTAL)
tree = ttk.Treeview(Body, columns=("Firstname", "Lastname", "Address"), selectmode="extended", height=300, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Firstname', text="Firstname", anchor=W)
tree.heading('Lastname', text="Lastname", anchor=W)
tree.heading('Address', text="Address", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=200)
tree.column('#2', stretch=NO, minwidth=0, width=200)
tree.column('#3', stretch=NO, minwidth=0, width=200)
tree.pack()

#==================================INITIALIZATION=====================================

if __name__ == '__main__':
    root.mainloop()

