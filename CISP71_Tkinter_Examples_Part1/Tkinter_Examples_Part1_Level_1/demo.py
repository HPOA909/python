from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.title("Button Displaying Message !!")
root.geometry('300x300')

heightLb=Label(root, text="Height")
widthLb=Label(root, text="Width")

heightEn=Entry(root)
widthEn=Entry(root)

path="C:/Users/szaki5/Desktop/CISP71_Tkinter_Examples_Part1/Tkinter_Examples_Part1_Level_1/icons/Superman-icon.png"
src_img= PhotoImage(file=path)
img=Label(root, image = src_img)

zoomInBt=Button(root,text='Zoom In')
zoomOutBt=Button(root,text='Zoom Out')

#create a checkbutton widget
CheckVar1 = IntVar()

aspectCb= Checkbutton(root,
                      text = "Reserve",
                      variable = CheckVar1, 
                      onvalue = 1, offvalue = 0 )

heightLb.grid(row=0,sticky=E)
widthLb.grid(row=1,sticky=E)
heightEn.grid(row=0, column=1)
widthEn.grid(row=1, column=1)
aspectCb.grid(columnspan=2, sticky=W)

img.grid(row=0, column=2, columnspan=2, rowspan=2,
               sticky=W+E+N+S, padx=5, pady=5)

zoomInBt.grid(row=2,column=2)
zoomOutBt.grid(row=2,column=3)

root.mainloop()

