#use sqlite with python
#This program is going to create a form to insert and show records of the address book sqlite table that we just created
##We are going to see how to delete a record from the database
# reference https://www.tutorialsteacher.com/python/database-crud-operation-in-python
#I did some modifications
# We are going to use Entry widgets and buttons
from tkinter import *

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

#add a function to clear the entry boxes
def clearFields():
    fNameEn.delete(0,END) 
    lNameEn.delete(0,END)
    addressEn.delete(0,END) 
    cityEn.delete(0,END)
    zipCodeEn.delete(0,END) 
    
#add functions to add record and display records

def addRecord():
    #connect to database
    #use placeholder variables and a dictionary
    conn=sqlite3.connect(path+"address_book.db")
    try:
        c=conn.cursor()
        c.execute("insert into contacts values (?,?,?,?,?,?)",
                  (fNameEn.get(),lNameEn.get(),addressEn.get(),cityEn.get(),selected.get(),int(zipCodeEn.get()) ))
        conn.commit()
        print ("one record added successfully")
         
    except:
         print("error in operation")
         conn.rollback()
    conn.close()
    clearFields()
    

def displayRecords():
    #connect to database
    #oid primary key
    #fetchall retrieves all records
    #fetchmany(50)
    #fetchone
    #records is a list of tuples inside it
    conn=sqlite3.connect(path+"address_book.db")
    try:
        c=conn.cursor()
        c.execute("select *,oid from contacts")
        records=c.fetchall()
        #as you see the records is a list with tuples inside it
        print(records)
        
        #loop throu results
        print_records=''
        for record in records:
            print_records +=str(record[0])+" "+ str(record[1])+" "+str(record[2])+"\n"
        query_label=Label(root,text=print_records)
        query_label.grid(row=10,column=0,columnspan=2)
        
        #commit changes
        conn.commit()
        #close connection
        conn.close()
                 
    except:
         print("error in operation")
         conn.rollback()
    conn.close()
    clearFields()
    
def deleteRecord():
    #connect to database
    #use placeholder variables and a dictionary
    conn=sqlite3.connect(path+"address_book.db")
    qry="DELETE from contacts where fName=?;"
    try:
        c=conn.cursor()
        c.execute(qry, (fNameEn.get(),))
        conn.commit()
        print ("record deleted successfully")
         
    except:
         print("error in operation")
         conn.rollback()
    conn.close()
    clearFields()

#create a list of states
stateList=["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY" ]

#We need to define the selected variable for our drop down list of states or option menu
selected=StringVar()

#set the default value for the option menu to the first item in the list 

selected.set(stateList[0])

#Create label widgets
fNameLb=Label(root,text="First Name")
lNameLb=Label(root,text="Last Name")
addressLb=Label(root,text="Address")
cityLb=Label(root,text="City")
stateLb=Label(root,text="State")
zipCodeLb=Label(root,text="Zip Code")

#Create Entry and DropDown widgets
fNameEn = Entry(root)
lNameEn = Entry(root)
addressEn=Entry(root)
cityEn=Entry(root)
zipCodeEn=Entry(root)

#create an OptionMenu widget -drop down list for the state
#recall *stateList -- unpack the list you declared
stateOp=OptionMenu(root,selected,*stateList)

#create two button widgets
addBt=Button(root,text="Add Record", command=addRecord)

displayBt=Button(root,text="Display Records", command=displayRecords)
deleteBt=Button(root,text="Delete Record", command=deleteRecord)

#specify where on the grid you are going to add those label widgets
fNameLb.grid(row=0, column=0)
lNameLb.grid(row=1, column=0)
addressLb.grid(row=2, column=0)
cityLb.grid(row=3, column=0)
stateLb.grid(row=4, column=0)
zipCodeLb.grid(row=5, column=0)

#specify where on the grid you are going to add the entry widgets
fNameEn.grid(row=0, column=1)
lNameEn.grid(row=1, column=1)
addressEn.grid(row=2, column=1)
cityEn.grid(row=3, column=1)
stateOp.grid(row=4, column=1)
zipCodeEn.grid(row=5, column=1)

#specify where on the grid you are going to add the button widgets
addBt.grid(row=7, column=0)
displayBt.grid(row=7, column=1)
deleteBt.grid(row=8, column=0)







#call the mainloop 
root.mainloop()
