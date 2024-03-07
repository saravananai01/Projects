import os
from tkinter import *
import tkinter as tk
from tkinter import ttk
from db.mydbfile import *
import mysql.connector 

root_student=Tk()
root_student.title("Student Management System")
root_student.geometry("600x600")
root_student.state("zoomed")
root_student.wm_iconbitmap("sms2.ico")

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

#  DB Connection :
mydbcon=DBManipulate()

# Db Connection Insert :
def inserttodb():
    student_name=ety_stdname.get()
    student_age=ety_stdage.get()
    st_mk_tam=ety_stdtam.get()
    st_mk_eng=ety_stdeng.get()
    st_mk_math=ety_stdmath.get()
    st_mk_sci=ety_stdsci.get()
    st_mk_ss=ety_stdss.get()

    x=mydbcon.insertvalues(student_name,student_age,st_mk_tam,st_mk_eng,st_mk_math,st_mk_sci,st_mk_ss)
    lblconmsg.config(text=x)
    selectdatas()

def selectdatas():
    data=mydbcon.mydbconnection()
    result=data.cursor()
    result.execute("select * from Student_Mark_List")
    i=0
    for ai_saravanan in result:
      for j in range(len(ai_saravanan)):
          lbldisplay=Entry(resultframe,width=10,fg="blue")
          lbldisplay.grid(row=i,column=j)
          lbldisplay.insert(END,ai_saravanan[j])
      i=i+1

# Db Connection Update :
def updatetodb():
    student_S_no=ety_std_s_no.get()
    student_name1=ety_stdname1.get()
    student_age1=ety_stdage1.get()
    st_mk_tam1=ety_stdtam1.get()
    st_mk_eng1=ety_stdeng1.get()
    st_mk_math1=ety_stdmath1.get()
    st_mk_sci1=ety_stdsci1.get()
    st_mk_ss1=ety_stdss1.get()

    y=mydbcon.updatevalue(student_S_no,student_name1,student_age1,st_mk_tam1,st_mk_eng1,st_mk_math1,st_mk_sci1,st_mk_ss1)
    lblconmsg1.config(text=y)
    selectdatas2()

def selectdatas2():
    data=mydbcon.mydbconnection()
    result=data.cursor()
    result.execute("select * from Student_Mark_List")
    i=0
    for ai_saravanan in result:
      for j in range(len(ai_saravanan)):
          lbldisplay=Entry(resultframe1,width=10,fg="blue")
          lbldisplay.grid(row=i,column=j)
          lbldisplay.insert(END,ai_saravanan[j])
      i=i+1

def delete():
    dlt_std_S_no=ety_std_sno.get()
    x2=mydbcon.deletevalue(dlt_std_S_no)
    lblconmsg2.config(text=x2)
    selectdatas1()
def selectdatas1():
    data=mydbcon.mydbconnection()
    result=data.cursor()
    result.execute("select * from Student_Mark_List")
    i=0
    for ai_saravanan in result:
      for j in range(len(ai_saravanan)):
          lbldisplay=Entry(resultframe2,width=10,fg="blue")
          lbldisplay.grid(row=i,column=j)
          lbldisplay.insert(END,ai_saravanan[j])
      i=i+1

# Menu Bar :
menulist=Menu(root_student)
  # File Menu :
filemenu=Menu(menulist,tearoff=0)
menulist.add_cascade(label="File",underline=0,accelerator="Alt+F",font=("Times New Roman", 10),menu=filemenu)  
filemenu.add_command(label="New",underline=0,accelerator="Ctrl+N",font=("Times New Roman", 10))
filemenu.add_command(label="Open...",underline=0,accelerator="Ctrl+O",font=("Times New Roman", 10))
filemenu.add_command(label="Save",underline=0,accelerator="Ctrl+S",font=("Times New Roman", 10))
filemenu.add_command(label="Save As...",underline=4,font=("Times New Roman", 10))
filemenu.add_separator()
filemenu.add_command(label="Page Setup...",underline=7,font=("Times New Roman", 10))
filemenu.add_command(label="Print",underline=0,accelerator="Ctrl+P",font=("Times New Roman", 10))
filemenu.add_separator()
filemenu.add_command(label="Exit",underline=1,accelerator="Ctrl+Q",command=Quit,font=("Times New Roman", 10))


  # Edit Menu :
editmenu=Menu(menulist,tearoff=0)
menulist.add_cascade(label="Edit",underline=0,accelerator="Alt+E",menu=editmenu,font=("Times New Roman", 10))
editmenu.add_command(label="Undo",underline=0,accelerator="Ctrl+Z",font=("Times New Roman", 10))
editmenu.add_separator()
editmenu.add_command(label="Cut",underline=2,accelerator="Ctrl+X",font=("Times New Roman", 10))
editmenu.add_command(label="Copy",underline=0,accelerator="Ctrl+C",font=("Times New Roman", 10))
editmenu.add_command(label="Paste",underline=0,accelerator="Ctrl+v",font=("Times New Roman", 10))
editmenu.add_command(label="Delete",underline=2,accelerator="Del",font=("Times New Roman", 10))
editmenu.add_separator()
editmenu.add_command(label="Find...",underline=0,accelerator="Ctrl+F",font=("Times New Roman", 10))
editmenu.add_command(label="Find Next",underline=4,accelerator="F3",font=("Times New Roman", 10))
editmenu.add_command(label="Replace...",underline=0,accelerator="Ctrl+H",font=("Times New Roman", 10))
editmenu.add_command(label="Go To...",underline=0,accelerator="Ctrl+G",font=("Times New Roman", 10))
editmenu.add_separator()
editmenu.add_command(label="Select All",underline=6,accelerator="Ctrl+A",font=("Times New Roman", 10))
editmenu.add_command(label="Date/Time",underline=5,accelerator="F5",font=("Times New Roman", 10))

  # Format Bar :
formatmenu=Menu(menulist,tearoff=0)
menulist.add_cascade(label="Format",underline=1,accelerator="Alt+O",menu=formatmenu,font=("Times New Roman", 10))
formatmenu.add_command(label="Word Wrap...",underline=0,font=("Times New Roman", 10))
formatmenu.add_command(label="Font...",underline=0,font=("Times New Roman", 10)) 

  # View Menu :
viewmenu=Menu(menulist,tearoff=0)
menulist.add_cascade(label="View",underline=0,accelerator="Alt+V",menu=viewmenu,font=("Times New Roman", 10))
viewmenu.add_command(label="Status Bar",underline=0,font=("Times New Roman", 10))

  # Help Menu :
helpmenu=Menu(menulist,tearoff=0)
menulist.add_cascade(label="Help",underline=0,accelerator="Alt+H",menu=helpmenu,font=("Times New Roman", 10))
helpmenu.add_command(label="View Hepl",underline=4,font=("Times New Roman", 10))
helpmenu.add_command(label="About Notepad",underline=0,command=about,font=("Times New Roman", 10))
root_student.config(menu=menulist)

  # Image Adding :
imgdir1=os.path.join((os.path.join(os.path.dirname(__file__),'img')),"banner.gif")
getTitleImage=PhotoImage('titleimage',file=imgdir1)

# imageframe=Frame(root_student,bg="black")
# imageframe.pack(padx=10,fill="x")

lbltitileframe=Label(root_student,image=getTitleImage).pack()

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
lbl_stdage=Label(tabdisplayinframe,text="Student Age ",font=("Times New Roman", 10))
lbl_stdage.grid(pady=10,row=2,column=1)
lbl_stdtamil=Label(tabdisplayinframe,text="Tamil",font=("Times New Roman", 10))
lbl_stdtamil.grid(pady=10,row=3,column=1)
lbl_stdeng=Label(tabdisplayinframe,text="English",font=("Times New Roman", 10))
lbl_stdeng.grid(pady=10,row=4,column=1)
lbl_stdmath=Label(tabdisplayinframe,text="Maths",font=("Times New Roman", 10))
lbl_stdmath.grid(pady=10,row=5,column=1)
lbl_stdscie=Label(tabdisplayinframe,text="Science",font=("Times New Roman", 10))
lbl_stdscie.grid(pady=10,row=6,column=1)
lbl_stds_s=Label(tabdisplayinframe,text="Social_Science",font=("Times New Roman", 10))
lbl_stds_s.grid(pady=10,row=7,column=1)
  
  # Value Entry ;
ety_stdname=Entry(tabdisplayinframe)
ety_stdname.grid(padx=10,pady=10,row=1,column=2)
ety_stdage=Entry(tabdisplayinframe)
ety_stdage.grid(padx=10,pady=10,row=2,column=2)
ety_stdtam=Entry(tabdisplayinframe)
ety_stdtam.grid(padx=10,pady=10,row=3,column=2)
ety_stdeng=Entry(tabdisplayinframe)
ety_stdeng.grid(padx=10,pady=10,row=4,column=2)
ety_stdmath=Entry(tabdisplayinframe)
ety_stdmath.grid(padx=10,pady=10,row=5,column=2)
ety_stdsci=Entry(tabdisplayinframe)
ety_stdsci.grid(padx=10,pady=10,row=6,column=2)
ety_stdss=Entry(tabdisplayinframe)
ety_stdss.grid(padx=10,pady=10,row=7,column=2)

  # Button Create :
btninsert=Button(tabdisplayinframe,text='Insert',font=("Times New Roman", 10),activebackground="blue",activeforeground="red",command=inserttodb)
btninsert.grid(row=10,column=1)
# btnselc=Button(tabdisplayinframe,text="Select",font=("Times New Roman", 10),activebackground="blue",activeforeground="red",command=selectdatas)
# btnselc.grid(row=10,column=2)
btnclear=Button(tabdisplayinframe,text="Clear",font=("Times New Roman", 10),activebackground="blue",activeforeground="red")
btnclear.grid(row=10,column=2)
btnExit=Button(tabdisplayinframe,text="Exit",font=("Times New Roman", 10),activebackground="blue",activeforeground="red",command=Quit)
btnExit.grid(row=10,column=3)

  # Db connect :
# msg=mydbcon.returnMsg()
lblconmsg=Label(tabdisplayinframe,text="",font=("Times New Roman", 10))
lblconmsg.grid(row=11,column=2,pady=20)

resultframe=Frame(tabdisplayinframe,width=800,height=600,bg="black")
resultframe.grid(row=12,columnspan=5)

# Upade :
tabdisplayinframe=Frame(tabupdate,width=root_student.winfo_screenwidth(),height=root_student.winfo_screenheight())
tabdisplayinframe.pack()

  # Title Create :
lbl_stdtitile1=Label(tabdisplayinframe,text="Updating Student Details :",font=("Times New Roman", 10))
lbl_stdtitile1.grid(pady=10,row=0,columnspan=10)
lbl_std_S_no=Label(tabdisplayinframe,text="S_No",font=("Times New Roman", 10))
lbl_std_S_no.grid(pady=10,row=1,column=1)
lbl_stdname1=Label(tabdisplayinframe,text="Name Of The Student",font=("Times New Roman", 10))
lbl_stdname1.grid(pady=10,row=2,column=1)
lbl_stdage1=Label(tabdisplayinframe,text="Student Age ",font=("Times New Roman", 10))
lbl_stdage1.grid(pady=10,row=3,column=1)
lbl_stdtamil1=Label(tabdisplayinframe,text="Tamil",font=("Times New Roman", 10))
lbl_stdtamil1.grid(pady=10,row=4,column=1)
lbl_stdeng1=Label(tabdisplayinframe,text="English",font=("Times New Roman", 10))
lbl_stdeng1.grid(pady=10,row=5,column=1)
lbl_stdmath1=Label(tabdisplayinframe,text="Maths",font=("Times New Roman", 10))
lbl_stdmath1.grid(pady=10,row=6,column=1)
lbl_stdscie1=Label(tabdisplayinframe,text="Science",font=("Times New Roman", 10))
lbl_stdscie1.grid(pady=10,row=7,column=1)
lbl_stds_s1=Label(tabdisplayinframe,text="Social_Science",font=("Times New Roman", 10))
lbl_stds_s1.grid(pady=10,row=8,column=1)
  
  # Value Entry ;
ety_std_s_no=Entry(tabdisplayinframe)
ety_std_s_no.grid(padx=10,pady=10,row=1,column=2)
ety_stdname1=Entry(tabdisplayinframe)
ety_stdname1.grid(padx=10,pady=10,row=2,column=2)
ety_stdage1=Entry(tabdisplayinframe)
ety_stdage1.grid(padx=10,pady=10,row=3,column=2)
ety_stdtam1=Entry(tabdisplayinframe)
ety_stdtam1.grid(padx=10,pady=10,row=4,column=2)
ety_stdeng1=Entry(tabdisplayinframe)
ety_stdeng1.grid(padx=10,pady=10,row=5,column=2)
ety_stdmath1=Entry(tabdisplayinframe)
ety_stdmath1.grid(padx=10,pady=10,row=6,column=2)
ety_stdsci1=Entry(tabdisplayinframe)
ety_stdsci1.grid(padx=10,pady=10,row=7,column=2)
ety_stdss1=Entry(tabdisplayinframe)
ety_stdss1.grid(padx=10,pady=10,row=8,column=2)

  # Button Create :
btnupdate=Button(tabdisplayinframe,text='Update',font=("Times New Roman", 10),activebackground="blue",activeforeground="red",command=updatetodb)
btnupdate.grid(row=11,column=1)
# btnclear1=Button(tabdisplayinframe,text="Select",font=("Times New Roman", 10),activebackground="blue",activeforeground="red",command=selectdatas)
# btnclear1.grid(row=11,column=2)
btnclear=Button(tabdisplayinframe,text="Clear",font=("Times New Roman", 10),activebackground="blue",activeforeground="red")
btnclear.grid(row=11,column=2)
btnExit=Button(tabdisplayinframe,text="Exit",font=("Times New Roman", 10),activebackground="blue",activeforeground="red",command=Quit)
btnExit.grid(row=11,column=3)

  # Db connect :
# msg=mydbcon.returnMsg()
lblconmsg1=Label(tabdisplayinframe,text="",font=("Times New Roman", 10))
lblconmsg1.grid(row=12,column=2,pady=20)

resultframe1=Frame(tabdisplayinframe,width=800,height=600,bg="black")
resultframe1.grid(row=13,columnspan=5)


# Delete :
tabdisplayinframe=Frame(tabDelete,width=root_student.winfo_screenwidth(),height=root_student.winfo_screenheight())
tabdisplayinframe.pack()


# Titile Creating :
frme_ttl=Label(tabdisplayinframe,text="Deleting Studen Name :",font=("Times New Roman", 10))
frme_ttl.grid(pady=10,row=0,columnspan=10)
dlt_std_S_no=Label(tabdisplayinframe,text="S_No",font=("Times New Roman", 10))
dlt_std_S_no.grid(pady=10,row=2,column=1)
# dlt_std_st_name=Label(tabdisplayinframe,text="Name Of The Student",font=("Times New Roman", 10))
# dlt_std_st_name.grid(pady=10,row=3,column=1)

# Value Entry :
ety_std_sno=Entry(tabdisplayinframe)
ety_std_sno.grid(padx=10,row=2,column=2)
# ety_std_name=Entry(tabdisplayinframe)
# ety_std_name.grid(padx=10,row=3,column=2)
#  Button :
dlt_btn1=Button(tabdisplayinframe,text="Delete",font=("Times New Roman", 10),activebackground="blue",activeforeground="red",command=delete)
dlt_btn1.grid(padx=10,row=13,column=2)
clr_btn1=Button(tabdisplayinframe,text="Clear",font=("Times New Roman", 10),activebackground="blue",activeforeground="red",command=Quit)
clr_btn1.grid(row=13,column=3,padx=10,pady=10)

# Db Connect Msg:
lblconmsg2=Label(tabdisplayinframe,text="",font=("Times New Roman", 10))
lblconmsg2.grid(row=14,column=2,pady=10)

resultframe2=Frame(tabdisplayinframe,width=800,height=600,bg="black")
resultframe2.grid(row=15,columnspan=5)

selectdatas()
selectdatas1()
selectdatas2()
root_student.mainloop()