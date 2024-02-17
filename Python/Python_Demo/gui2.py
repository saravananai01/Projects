from tkinter import *
from tkinter import ttk
import tkinter as tk

aathar=Tk()
aathar.title("Verify")
aathar.geometry("600x600")

# Name Detais:
Label(aathar,text="Fisrt_Name").grid(row=1,column=0)
Label(aathar,text="Last_Name").grid(row=2,column=0)
f1=Entry(aathar)
f2=Entry(aathar)
f1.grid(row=1,column=1)
f2.grid(row=2,column=1)

# Gender :
var1=IntVar
Checkbutton(aathar,text="Male",variable=var1).grid(row=3,column=0,sticky=W)
var2=IntVar
Checkbutton(aathar,text="Female",variable=var2).grid(row=3,column=1,sticky=W)
var3=IntVar
Checkbutton(aathar,text="Transgender").grid(row=3,column=2,sticky=W)

# DOB : 
ttk.Label(aathar,text="Date_Of_Birth").grid(row=6,column=0,padx=10,pady=25)
d=tk.StringVar()
dobchoosen=ttk.Combobox(aathar,width=27,textvariable=d)
dobchoosen['value']=('1','2','3','4','5','6','7','8','9','10')
dobchoosen.grid(row=6,column=1)



# Status Bar :
menu =Menu(aathar)
aathar.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="open")
filemenu.add_command(label="Edit")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=aathar.quit)

# Lable :
ttk.Label(aathar,text="Select Your State :",font=("Times New Roman", 10)).grid(row=8,column=0,padx=10,pady=25)

# ComboBox Creation :
n=tk.StringVar()
statechoosen=ttk.Combobox(aathar,width=27,textvariable=n)

# Added ComboBox Drop Down List :
statechoosen['value']=('Tamilnadu','Kerala','Karnataka','Andhra')
statechoosen.grid(row=8,column=1)

dobchoosen.current()
statechoosen.current()
aathar.mainloop()