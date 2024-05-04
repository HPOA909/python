from tkinter import *
from PIL import ImageTk,Image
import sqlite3
#create the main window
root=Tk()
#give the window a title
root.title("Having fun with sqlite")

#change the size of the window
root.geometry("300x300")

path="C:/Users/szaki5/Desktop/CISP71_Tkinter_SQLite_Examples/CISP71_Tkinter_SQLite_Examples_Part_1/"

#changing the icon of the window
root.iconbitmap(path+"icons/Boss.ico")

conn=sqlite3.connect(path+"Address_Book.db")
try:
        #create a cursor this will send orders to the database
        c=conn.cursor()

        #create a table - columns and rows
        #we use our cursor to do that. The cursor will execute a sql command to do that
        #since sql command to create a table will be long
        #we are going to use triple quotes to allow us to write on more than one line
        #Cool thing about sqlite it has three data types
        #text, null, integer, real ,blob (image files, video files)
        #https://www.sqlite.org/datatype3.html
        
        c.execute('''CREATE TABLE contacts (     
        fName TEXT ,
        lName text ,
        address text ,
        city text,
        state text ,
        zipCode integer);''')
        print ('table created successfully')
except:
        print ('error in operation')
        conn.rollback()
#Close Connection
conn.close()

root.mainloop()