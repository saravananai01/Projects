from tkinter import *
import tkinter as tk
import mysql.connector
details=tk.Tk()
details.title("Studens Details")
details.geometry("700x700")


# Class :
def MyDBConnection():
    dbcon=mysql.connector.connect(
    host="192.168.1.240",
    user="AIBATCH01",
    password="AI@123",
    database="ai_saravanan"
    )

    return dbcon
    # print("connect to database",dbcon)

def quit():
    details.destroy()

def aboutpage():
    abt=tk.Tk()
    abt.title("About us")
    abt.geometry("300x300")
    """Welcome to parent window
    created on : 21-02-2024
    by Karthick AG
    """
    message="""Welcome to parent window
    created on : 22-02-2024
    by "DARGO"
    """
    lntinfo=tk.Label(abt,text=message)
    lntinfo.pack()
    abt.mainloop()

def insert():
    a=vlinput1.get()
    b=vlinput2.get()
    c=vlinput3.get()
    d=vlinput4.get()
    e=vlinput5.get()
    f=vlinput6.get()
    g=vlinput7.get()
    e_con=MyDBConnection()
    result=e_con.cursor()
    statement="insert into Student_Mark_List(Name,Age,Tamil,English,Maths,Science,Social_Science) value(%s,%s,%s,%s,%s,%s,%s);"
    valuepass=(a,b,c,d,e,f,g)
    result.execute(statement,valuepass)
    e_con.commit()
    msg=result.rowcount,"row Insert"
    stoutput2.config(text=a)
    stoutput3.config(text=b)
    stoutput4.config(text=c)
    stoutput5.config(text=d)
    stoutput6.config(text=e)
    stoutput7.config(text=f)
    stoutput8.config(text=g)
    stoutput9.config(text=msg)

def upadte():
    a=vlinput1.get()
    b=vlinput2.get()
    c=vlinput3.get()
    d=vlinput4.get()
    e=vlinput5.get()
    f=vlinput6.get()
    g=vlinput7.get()
    h=vlinput8.get()
    e_con=MyDBConnection()
    result=e_con.cursor()
    statement="update Student_Mark_List set Age=(%s) where S_no=(%s);"
    valuepass=(b,h)
    result.execute(statement,valuepass)
    e_con.commit()
    msg1=result.rowcount,"row updated"
    stoutput2.config(text=a)
    stoutput3.config(text=b)
    stoutput4.config(text=c)
    stoutput5.config(text=d)
    stoutput6.config(text=e)
    stoutput7.config(text=f)
    stoutput8.config(text=g)
    stoutput9.config(text=msg1)

def delete():
    h=vlinput8.get()
    e_con=MyDBConnection()
    result=e_con.cursor()
    statement="deleted from Student_Mark_List S_no=(%s);"
    valuepass=(h,)
    result.execute(statement,valuepass)
    e_con.commit()
    msg1=result.rowcount,"row deleted"
    stoutput9.config(text=msg1)

def clear():
    a=" "
    b=" "
    c=" "
    d=" "
    e=" "
    f=" "
    g=" "
    stoutput2.config(text=a)
    stoutput3.config(text=b)
    stoutput4.config(text=c)
    stoutput5.config(text=d)
    stoutput6.config(text=e)
    stoutput7.config(text=f)
    stoutput8.config(text=g)
    

# Name Creating :
lbltit1=Label(details,text="Name: ",font=("Times New Roman", 10))
lbltit1.grid(row=1,column=0)
lbltit2=Label(details,text="Age: ",font=("Times New Roman", 10))
lbltit2.grid(row=2,column=0)
lbltit3=Label(details,text="Tamil: ",font=("Times New Roman", 10))
lbltit3.grid(row=3,column=0)
lbltit4=Label(details,text="English:",font=("Times New Roman", 10))
lbltit4.grid(row=4,column=0)
lbltit5=Label(details,text="Maths:",font=("Times New Roman", 10))
lbltit5.grid(row=5,column=0)
lbltit6=Label(details,text="Science:",font=("Times New Roman", 10))
lbltit6.grid(row=6,column=0)
lbltit7=Label(details,text="Social Science:",font=("Times New Roman", 10))
lbltit7.grid(row=7,column=0)
lbltit8=Label(details,text="S_no :",font=("Times New Roman",10))
lbltit8.grid(row=8,column=0)

# Value Entery :
vlinput1=Entry(details,width=20)
vlinput1.grid(row=1,column=2)
vlinput2=Entry(details,width=20)
vlinput2.grid(row=2,column=2)
vlinput3=Entry(details,width=20)
vlinput3.grid(row=3,column=2)
vlinput4=Entry(details,width=20)
vlinput4.grid(row=4,column=2)
vlinput5=Entry(details,width=20)
vlinput5.grid(row=5,column=2)
vlinput6=Entry(details,width=20)
vlinput6.grid(row=6,column=2)
vlinput7=Entry(details,width=20)
vlinput7.grid(row=7,column=2)
vlinput8=Entry(details,width=20)
vlinput8.grid(row=8,column=2)

# Show OutPut :
stoutput1=Label(details,text="Your Result :",font=("Times New Roman", 10))
stoutput1.grid(row=12,column=15)
stoutput2=Label(details,text=" ",font=("Times New Roman", 10))
stoutput2.grid(row=13,column=15)
stoutput3=Label(details,text=" ",font=("Times New Roman", 10))
stoutput3.grid(row=14,column=15)
stoutput4=Label(details,text=" ",font=("Times New Roman", 10))
stoutput4.grid(row=15,column=15)
stoutput5=Label(details,text=" ",font=("Times New Roman", 10))
stoutput5.grid(row=16,column=15)
stoutput6=Label(details,text=" ",font=("Times New Roman", 10))
stoutput6.grid(row=17,column=15)
stoutput7=Label(details,text=" ",font=("Times New Roman", 10))
stoutput7.grid(row=18,column=15)
stoutput8=Label(details,text=" ",font=("Times New Roman", 10))
stoutput8.grid(row=19,column=15)
stoutput9=Label(details,text=" ",font=("Times New Roman", 10))
stoutput9.grid(row=20,column=15)

# Create Button :
insbtn=Button(details,text="Insert",font=("Times New Roman", 10),activebackground="blue",activeforeground="red",command=insert)
insbtn.grid(row=22,column=10)

updbtn=Button(details,text="Upadte",font=("Times New Roman", 10),activebackground="blue",activeforeground="red",command=upadte)
updbtn.grid(row=22,column=15)

dtlbtn=Button(details,text="Delete",font=("Times New Roman", 10),activebackground="blue",activeforeground="red",command=delete)
dtlbtn.grid(row=22,column=20)

clrbtn=Button(details,text="Clear",font=("Times New Roman", 10),activebackground="blue",activeforeground="red",command=clear)
clrbtn.grid(row=22,column=25)


# Menu Bar :
menubar=tk.Menu(details)
filemenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu,underline=0)
filemenu.add_command(label="New",underline=0,accelerator="Alt+N")
filemenu.add_command(label="New Window",underline=4,accelerator="Alt+W")
filemenu.add_command(label="Open",underline=0,accelerator="Alt+O")
filemenu.add_command(label="Save",underline=0,accelerator="Alt+S")
filemenu.add_command(label="Save As",underline=4,accelerator="Alt+A")
filemenu.add_separator()
filemenu.add_command(label="PageSetup",underline=7,accelerator="Alt+U")
filemenu.add_command(label="Print",underline=0,accelerator="Alt+P")
filemenu.add_separator()
filemenu.add_command(label="Exit",underline=1,command=quit,accelerator="Ctr+X")

# Edit Bar :
editmenu=tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Undo",  underline=0, accelerator="Ctr+Z")
editmenu.add_command(label="Redo",  underline=4, accelerator="Ctr+X")
editmenu.add_separator()
editmenu.add_command(label="Copy",  underline=0, accelerator="Ctr+C")
editmenu.add_command(label="Cut",  underline=0, accelerator="Ctr+X")
editmenu.add_command(label="Paste",  underline=0, accelerator="Ctr+V")

# View Bar:
viewmenu=tk.Menu(menubar)
menubar.add_cascade(label="View")

# Help Bar :
helpmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="About",  underline=0, accelerator="Alt+A", command=aboutpage)


details.config(menu=menubar)
details.mainloop()