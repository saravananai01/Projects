from tkinter import *

app=Tk()
app.title("My First Python Gui App")
app.geometry("500x200")
app.config(bg="grey")

def clickresult():
    a=10
    b=10
    c=a+b
    ibltittle.config(text=c,)

ibltittle=Label(app,text="Arithmetic Operation")
ibltittle.grid(row=0,column=1,padx=40,pady=40)
 
inputbox=Entry(app,width=60)
inputbox.grid(row=0,column=2)

ibltittle1=Label(app,text="Arithmetic Operation")
ibltittle1.grid(row=1,column=1,padx=40,pady=40)

inputbox1=Entry(app,width=60)
inputbox1.grid(row=1,column=2)

clickname=Button(app,text="Addition",command=clickresult,)
clickname.grid(row=2,column=2,padx=40,pady=40)

app.mainloop()


from tkinter import *

App1=Tk()
App1.titile("")
App1.geometry("1366x768")
App1.config(bg="black")

enibltitile=Label(app,text="Enter Your Name")
enibltitile.grid(row=0,column=2,padx=30,pady=30)

eninputbox=Entry(App1,width=50)
enibltitile.grid(row=1,column=2,padx=30,pady=30)

enibltitile1=Label(App1,text="Enter ")