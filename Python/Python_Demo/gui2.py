from tkinter import *

aathar=Tk()
aathar.title("Verify Aathar")
aathar.geometry("600x600")

# Name Detais:

Label(aathar,text="Fisrt_Name").grid(row=1,column=0)
Label(aathar,text="Last_Name").grid(row=2,column=0)
f1=Entry(aathar)
f2=Entry(aathar)
f1.grid(row=1,column=1)
f2.grid(row=2,column=1)

# Gender :

var1= IntVar
Checkbutton(aathar,text="Male",variable=var1).grid(row=3,sticky=W)
var2= IntVar
Checkbutton(aathar,text="Female",variable=var2).grid(row=4,sticky=W)
var3= IntVar
Checkbutton(aathar,text="Transgender").grid(row=5,sticky=W)

# DOB : 

Label(aathar,text="Enter Your Date_Of_Birth").grid(row=6,column=0)
b1=Entry(aathar)
b1.grid(row=6,column=1)

# State :
Label(aathar,text="Choose Your State :").grid(row=7)
menu=Menu(aathar)
aathar.config(menu=menu)
Statemenu =Menu(menu)
menu.add_cascade(label='State',menu=Statemenu)
Statemenu.add_command(label='Tamilnadu')
Statemenu.add_command(label='Kerala')
Statemenu.add_separator()
Statemenu.add_command(label='Karnataka',command=aathar.quit)
# lb=Listbox(aathar)
# lb.insert(1,'Tamilnadu')
# lb.insert(2,'Kerala')
# lb.insert(3,'Karnataka')
# lb.insert(4,'Andhra')
# lb.grid(row=8)

Statemenu.mainloop()