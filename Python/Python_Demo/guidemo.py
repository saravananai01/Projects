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

ibltittle1=Label(app,text="Arithmetic Operation",font="bold",fg="red")
ibltittle1.grid(row=1,column=1,padx=40,pady=40)

inputbox1=Entry(app,width=60)
inputbox1.grid(row=1,column=2)

clickname=Button(app,text="Addition",command=clickresult,)
clickname.grid(row=2,column=2,padx=40,pady=40)

app.mainloop()

from tkinter import *

calculation=Tk()
calculation.title("Calculater")
calculation.geometry("1366x768")

def Addition():
    a=int(tbentrya.get())
    b=int(tbentryb.get())
    c=a+b
    lbloutput1.config(text=c)

def Subtracted():
    a=int(tbentrya.get())
    b=int(tbentryb.get())
    c=a-b
    lbloutput1.config(text=c)

def Multiplication():
    a=int(tbentrya.get())
    b=int(tbentryb.get())
    c=a*b
    lbloutput1.config(text=c)

def Friends():
    a=(tbentrya.get())
    b=(tbentryb.get())
    lbloutput1.config(text=f"My Bond  :{a}")
    lbloutput2.config(text=f"My Blood :{b}")


lbltitile=Label(calculation,text="Arithmatic Operation")
lbltitile.grid(row=0,column=2,padx=30,pady=30)

lblmgs1=Label(calculation,text="Please Enter Value :")
lblmgs1.grid(row=1,column=2,padx=30,pady=30)

tbentrya=Entry(calculation,width=20)
tbentrya.grid(row=1,column=20,padx=30,pady=30)

lblmgs2=Label(calculation,text="Please Enter Value :")
lblmgs2.grid(row=2,column=2,padx=30,pady=30)

tbentryb=Entry(calculation,width=20)
tbentryb.grid(row=2,column=20,padx=30,pady=30)

lbloutput1=Label(calculation,text="Your Result :",font=("bold"))
lbloutput1.grid(row=3,column=30,padx=30,pady=30)

lbloutput2=Label(calculation,text="Your Result :",font=("bold"))
lbloutput2.grid(row=4,column=30,padx=30,pady=30)


btnadd=Button(calculation,text="Addition",command=Addition)
btnadd.grid(row=4,column=25)

btnsub=Button(calculation,text="Subtraction",command=Subtracted)
btnsub.grid(row=4,column=27)

btmult=Button(calculation,text="Multiplication",command=Multiplication)
btmult.grid(row=4,column=29)

btnfrd=Button(calculation,text="Frinds",command=Friends)
btnfrd.grid(row=4,column=4)

calculation.mainloop()