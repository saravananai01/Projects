from tkinter import *
import mysql.connector

app=Tk()
app.title("Insert into MYSQL DB Demo")
app.geometry("500x500")

# Frame Methods :
frameleft=Frame(app,bg="black",width=500,height=500,padx=30,pady=30)
frameleft.pack(side=LEFT)

frameright=Frame(app,bg="red",width=500,height=500)
frameright.pack(side=RIGHT)
lbl_titile_of_operation=Label(frameleft,text="Insert into MYSQL DB Demo")
lbl_titile_of_operation.grid(row=0,columnspan=5)

lblname=Label(frameleft,text="Name")
lblname.grid(row=2,column=1,padx=30,pady=10)
lbltamil=Label(frameleft,text="Tamil")
lbltamil.grid(row=3,column=1)


app.mainloop()