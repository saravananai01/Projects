import os
from tkinter import *
import tkinter as tk
from tkinter import ttk


root_student=Tk()
root_student.title("Student Management System")
root_student.geometry("600x600")
root_student.state("zoomed")
# root_student.wm_iconbitmap("")

def Quit():
    root_student.destroy()

def about():
    abt=tk.Tk()
    abt.title("About as")
    abt.geometry("300x300")
    """Welcome to parent window
    created on : 21-02-2024
    by Karthick AG
    """
    Message= """ Welcome to parent window
    created on : 26-02-2024
    by Darko
    """
    darko=tk.Label(abt,text=Message)
    darko.pack()
    abt.mainloop()

# Menu Bar :
menulist=Menu(root_student)
  # File Menu :
filemenu=Menu(menulist,tearoff=0)
menulist.add_cascade(label="File",underline=0,accelerator="Alt+F",menu=filemenu)  
filemenu.add_command(label="New",underline=0,accelerator="Ctrl+N")
filemenu.add_command(label="Open...",underline=0,accelerator="Ctrl+O")
filemenu.add_command(label="Save",underline=0,accelerator="Ctrl+S")
filemenu.add_command(label="Save As...",underline=4)
filemenu.add_separator()
filemenu.add_command(label="Page Setup...",underline=7)
filemenu.add_command(label="Print",underline=0,accelerator="Ctrl+P")
filemenu.add_separator()
filemenu.add_command(label="Exit",underline=1,accelerator="Ctrl+Q",command=Quit)

  # Edit Menu :
editmenu=Menu(menulist,tearoff=0)
menulist.add_cascade(label="Edit",underline=0,accelerator="Alt+E",menu=editmenu)
editmenu.add_command(label="Undo",underline=0,accelerator="Ctrl+Z")
editmenu.add_separator()
editmenu.add_command(label="Cut",underline=2,accelerator="Ctrl+X")
editmenu.add_command(label="Copy",underline=0,accelerator="Ctrl+C")
editmenu.add_command(label="Paste",underline=0,accelerator="Ctrl+v")
editmenu.add_command(label="Delete",underline=2,accelerator="Del")
editmenu.add_separator()
editmenu.add_command(label="Find...",underline=0,accelerator="Ctrl+F")
editmenu.add_command(label="Find Next",underline=4,accelerator="F3")
editmenu.add_command(label="Replace...",underline=0,accelerator="Ctrl+H")
editmenu.add_command(label="Go To...",underline=0,accelerator="Ctrl+G")
editmenu.add_separator()
editmenu.add_command(label="Select All",underline=6,accelerator="Ctrl+A")
editmenu.add_command(label="Date/Time",underline=5,accelerator="F5")

  # Format Bar :
formatmenu=Menu(menulist,tearoff=0)
menulist.add_cascade(label="Format",underline=1,accelerator="Alt+O",menu=formatmenu)
formatmenu.add_command(label="Word Wrap...",underline=0)
formatmenu.add_command(label="Font...",underline=0) 

  # View Menu :
viewmenu=Menu(menulist,tearoff=0)
menulist.add_cascade(label="View",underline=0,accelerator="Alt+V",menu=viewmenu)
viewmenu.add_command(label="Status Bar",underline=0)

  # Help Menu :
helpmenu=Menu(menulist,tearoff=0)
menulist.add_cascade(label="Help",underline=0,accelerator="Alt+H",menu=helpmenu)
helpmenu.add_command(label="View Hepl",underline=4)
helpmenu.add_command(label="About Notepad",underline=0,command=about)
root_student.config(menu=menulist)

  # Image Adding :
# imgdir1=os.path.join((os.path.join(os.path.dirname(__file__),'img')),"sms.gif")
# getTitleImage=PhotoImage('titleimage',file=imgdir1)

# imageframe=Frame(root_student,bg="black")
# imageframe.pack(padx=10,fill="x")

# lbltitileframe=Label(imageframe,image=getTitleImage).pack()

  # Tab Create :
tablist=ttk.Notebook(root_student)
tablist.pack(padx=10,pady=5)

  #  Tab Frame Create :
tabInsert=ttk.Frame(tablist,width=root_student.winfo_screenwidth(),height=root_student.winfo_screenheight())
tabInsert.pack()
tabupdate=ttk.Frame(tablist,width=root_student.winfo_screenwidth(),height=root_student.winfo_screenheight())
tabupdate.pack()
tabDelete=ttk.Frame(tablist,width=root_student.winfo_screenwidth(),height=root_student.winfo_screenheight())
tabDelete.pack()
tablist.add(tabInsert,text="Insert")
tablist.add(tabupdate,text="Update")
tablist.add(tabDelete,text="Delete")

tabdisplayinframe=Frame(tabInsert,width=root_student.winfo_screenwidth(),height=root_student.winfo_screenheight())
tabdisplayinframe.pack()

  # Title Create :
lbl_stdtitile=Label(tabdisplayinframe,text="Inserting Student Details :",font=("Times New Roman", 10))
lbl_stdtitile.grid(pady=10,row=0,columnspan=10)
lbl_stdname=Label(tabdisplayinframe,text="Name Of The Student",font=("Times New Roman", 10))
lbl_stdname.grid(pady=10,row=1,column=1)
lbl_stdtamil=Label(tabdisplayinframe,text="Tamil",font=("Times New Roman", 10))
lbl_stdtamil.grid(pady=10,row=2,column=1)
lbl_stdeng=Label(tabdisplayinframe,text="English",font=("Times New Roman", 10))
lbl_stdeng.grid(pady=10,row=3,column=1)
lbl_stdmath=Label(tabdisplayinframe,text="Maths",font=("Times New Roman", 10))
lbl_stdmath.grid(pady=10,row=4,column=1)
lbl_stdscie=Label(tabdisplayinframe,text="Science",font=("Times New Roman", 10))
lbl_stdscie.grid(pady=10,row=5,column=1)
lbl_stds_s=Label(tabdisplayinframe,text="Social_Science",font=("Times New Roman", 10))
lbl_stds_s.grid(pady=10,row=6,column=1)
  
  # Value Entry ;
ety_stdname=Entry(tabdisplayinframe)
ety_stdname.grid(padx=10,pady=10,row=1,column=2)
ety_stdtam=Entry(tabdisplayinframe)
ety_stdtam.grid(padx=10,pady=10,row=2,column=2)
ety_stdeng=Entry(tabdisplayinframe)
ety_stdeng.grid(padx=10,pady=10,row=3,column=2)
ety_stdmath=Entry(tabdisplayinframe)
ety_stdmath.grid(padx=10,pady=10,row=4,column=2)
ety_stdsci=Entry(tabdisplayinframe)
ety_stdsci.grid(padx=10,pady=10,row=5,column=2)
ety_stdss=Entry(tabdisplayinframe)
ety_stdss.grid(padx=10,pady=10,row=6,column=2)

  # Button Create :
btninsert=Button(tabdisplayinframe,text='Insert',font=("Times New Roman", 10),activebackground="blue",activeforeground="red")
btninsert.grid(row=8,column=1)
btnclear=Button(tabdisplayinframe,text="Clear",font=("Times New Roman", 10),activebackground="blue",activeforeground="red")
btnclear.grid(row=8,column=2)
btnExit=Button(tabdisplayinframe,text="Exit",font=("Times New Roman", 10),activebackground="blue",activeforeground="red",command=Quit)
btnExit.grid(row=8,column=3)

root_student.mainloop()