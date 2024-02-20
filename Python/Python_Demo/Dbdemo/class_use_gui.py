from tkinter import *
import mysql.connector

app=Tk()
app.title("Studen_Mark_List")
app.geometry("300x300")

class manuplate:
    
    def __init__(self):
        frametop=Frame(app,bg="black",width=800,height=300,padx=10,pady=10)
        frametop.pack(side=TOP)
        btninsert=Button(frametop,text="Insert",activeforeground="red",activebackground="blue").pack(padx=10,pady=10)
        btnupdate=Button(frametop,text="Update",activeforeground="red",activebackground="blue").pack(padx=10,pady=10)
        btndelete=Button(frametop,text="Delete",activeforeground="red",activebackground="blue").pack(padx=10,pady=10)

run=manuplate()
app.mainloop()