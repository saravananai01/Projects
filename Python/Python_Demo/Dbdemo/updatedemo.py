import os
from tkinter import *
from tkinter import ttk
# from db.mydbfile import DBManipulate
#from db.mydbfile import DBManipulate as kk
#import tkinter as tk


root_window=Tk()

root_window.title("Student Management System")
root_window.geometry("500x500")
#root_window.state("zoomed")
# root_window.wm_iconbitmap('sms.ico')

#mydbcon=kk()
# mydbcon=DBManipulate()

def exitParent():
    root_window.destroy()



#initializing Main menu
menulist=Menu(root_window)

#initializing submenu
submenulist=Menu(menulist, tearoff=0)

#creating submenus list
submenulist.add_command(label="New File", underline=0, accelerator="Ctrl+N")
submenulist.add_command(label="New Project",  underline=7, accelerator="Ctrl+Shift+j")
submenulist.add_command(label="New Py File", underline=5, accelerator="Ctrl+N")


#list of main menu
filemenu=Menu(menulist, tearoff=0)
menulist.add_cascade(label="File", menu=filemenu)
filemenu.add_cascade(label="New", menu=submenulist)
filemenu.add_command(label="Exit", underline=1, accelerator="Ctrl+Q", command=exitParent)

#Attach menu to the parent root window
root_window.config(menu=menulist)


#passing through direct image location
#imgdir1=os.path.join((os.path.join(os.path.dirname(__file__),'img')),"banner.gif")
#getTitleImage=PhotoImage('titleimage',file=imgdir1)

# giving image through general location
imgdir=os.path.join(os.path.dirname(__file__),'img')
getTitleImage=PhotoImage('titleimage',file=os.path.join(imgdir,'banner.gif'))

titleImageFrame=Frame(root_window, bg="black")#, height=200)
titleImageFrame.pack(padx=10,fill="x")

#giving title as text
#titletext="SMS"
#lblDisplayTitleImage=Label(titleImageFrame,text=titletext).pack()

#giving title as Image
lblDisplayTitleImage=Label(titleImageFrame,image=getTitleImage).pack()

#adding list of tabs
tablist=ttk.Notebook(root_window)
tablist.pack(padx=10, pady=5)

#tabInsert=ttk.Frame(tablist, width=600, height=600) for manuall size in width and height property

#creating tab to adapt window size in width and height property ==> use this == > root_window.winfo_screenheight()
tabInsert=ttk.Frame(tablist, width=root_window.winfo_screenwidth(), height=root_window.winfo_screenheight())
tabInsert.pack()

tabUpdate=ttk.Frame(tablist, width=root_window.winfo_screenwidth(), height=root_window.winfo_screenheight())
tabUpdate.pack()

tabDelete=ttk.Frame(tablist, width=root_window.winfo_screenwidth(), height=root_window.winfo_screenheight())
tabDelete.pack()

tablist.add(tabInsert,text="Insert")
tablist.add(tabUpdate,text="Update")
tablist.add(tabDelete,text="Delete")


titledisplayframeintab=Frame(tabInsert,width=root_window.winfo_screenwidth(), height=root_window.winfo_screenheight())
titledisplayframeintab.pack()

lbl_insertTitle=Label(titledisplayframeintab, text="Inserting Student Details")
lbl_insertTitle.grid(pady=10,row=0, columnspan=10)

lbl_StdName=Label(titledisplayframeintab,text="Name of the student ")
lbl_StdName.grid(pady=10,row=1,column=1)
Ety_StdName=Entry(titledisplayframeintab)
Ety_StdName.grid(padx=10,pady=10,row=1, column=2)



lbl_StdMkTamil=Label(titledisplayframeintab,text="Tamil")
lbl_StdMkTamil.grid(pady=10,row=2,column=1)
Ety_StdMkTamil=Entry(titledisplayframeintab)
Ety_StdMkTamil.grid(padx=10,pady=10,row=2, column=2)


lbl_StdMkEng=Label(titledisplayframeintab,text="Eng")
lbl_StdMkEng.grid(pady=10,row=3,column=1)
Ety_StdMkEng=Entry(titledisplayframeintab)
Ety_StdMkEng.grid(padx=10,pady=10,row=3, column=2)

lbl_StdMkMath=Label(titledisplayframeintab,text="Math")
lbl_StdMkMath.grid(pady=10,row=4,column=1)
Ety_StdMkMath=Entry(titledisplayframeintab)
Ety_StdMkMath.grid(padx=10,pady=10,row=4, column=2)

lbl_StdMkSci=Label(titledisplayframeintab,text="Sci")
lbl_StdMkSci.grid(pady=10,row=5,column=1)
Ety_StdMkSci=Entry(titledisplayframeintab)
Ety_StdMkSci.grid(padx=10,pady=10,row=5, column=2)


lbl_StdMkSS=Label(titledisplayframeintab,text="SS")
lbl_StdMkSS.grid(pady=10,row=6,column=1)
Ety_StdMkSS=Entry(titledisplayframeintab)
Ety_StdMkSS.grid(padx=10,pady=10,row=6, column=2)

btn_Insert=Button(titledisplayframeintab, text="Insert")
btn_Insert.grid(row=7,column=1)

btn_Clear=Button(titledisplayframeintab, text="Clear")
btn_Clear.grid(row=7,column=2)

btn_Exit=Button(titledisplayframeintab, text="Quit", command=exitParent)
btn_Exit.grid(row=7,column=3)

# msg=mydbcon.returnMsg()
lblConMsg=Label(titledisplayframeintab, text=msg)
lblConMsg.grid(row=8,column=2, pady=20)





root_window.mainloop()