from tkinter import *
import mysql.connector

app=Tk()
app.title("Studen_Mark_List")
app.geometry("300x300")

def MyDBConnection():
    dbcon=mysql.connector.connect(
    host="192.168.1.240",
    user="AIBATCH01",
    password="AI@123",
    database="ai_saravanan"
    )

    return dbcon
class manuplate:
    
    def __init__(self):
        frametop=Frame(app,bg="black",width=800,height=300,padx=10,pady=10)
        frametop.pack(side=TOP)
        btninsert=Button(frametop,text="Insert",command=self.insert,activeforeground="red",activebackground="blue").pack(padx=10,pady=10)
        btnupdate=Button(frametop,text="Update",activeforeground="red",activebackground="blue").pack(padx=10,pady=10)
        btndelete=Button(frametop,text="Delete",activeforeground="red",activebackground="blue").pack(padx=10,pady=10)
    
    def insert(self):

        details1=Tk()
        details1.title("Insert Into DB Demo")
        details1.geometry("500x500")
    # Frame :
        frameinsert=Frame(details1,bg="black",width=800,height=500,padx=10,pady=10)
        frameinsert.pack(side=RIGHT)
        
        lbltit=Label(frameinsert,text="Insert Into DB Demo")
        lbltit.grid(row=0,columnspan=5)

        insbtn=Button(frameinsert,text="Insert",font=("Times New Roman", 10),activebackground="blue",activeforeground="red",command=self)
        insbtn.grid(row=15,column=1)
        # Name Creating :
        Name1=Label(frameinsert,text="Name: ",font=("Times New Roman", 10))
        Name1.grid(row=1,columns=1)
        Age1=Label(frameinsert,text="Age: ",font=("Times New Roman", 10))
        Age1.grid(row=2,column=1)
        Tamil1=Label(frameinsert,text="Tamil: ",font=("Times New Roman", 10))
        Tamil1.grid(row=3,column=1)
        English1=Label(frameinsert,text="English:",font=("Times New Roman", 10))
        English1.grid(row=4,column=1)
        Maths1=Label(frameinsert,text="Maths:",font=("Times New Roman", 10))
        Maths1.grid(row=5,column=1)
        Science1=Label(frameinsert,text="Science:",font=("Times New Roman", 10))
        Science1.grid(row=6,column=1)
        S_Scince1=Label(frameinsert,text="Social Science:",font=("Times New Roman", 10))
        S_Scince1.grid(row=7,column=1)
        S_no1=Label(frameinsert,text="S_no :",font=("Times New Roman",10))
        S_no1.grid(row=8,column=1)

    # Value Entery :
        Name=Entry(frameinsert,width=20)
        Name.grid(row=1,column=2)
        Age=Entry(frameinsert,width=20)
        Age.grid(row=2,column=2)
        Tamil=Entry(frameinsert,width=20)
        Tamil.grid(row=3,column=2)
        English=Entry(frameinsert,width=20)
        English.grid(row=4,column=2)
        Maths=Entry(frameinsert,width=20)
        Maths.grid(row=5,column=2)
        Scince=Entry(frameinsert,width=20)
        Scince.grid(row=6,column=2)
        S_Scince=Entry(frameinsert,width=20)
        S_Scince.grid(row=7,column=2)
        S_no=Entry(frameinsert,width=20)
        S_no.grid(row=8,column=2)

    # show Output:
        stoutput1=Label(frameinsert,text="Your Result :",font=("Times New Roman", 10))
        stoutput1.grid(row=12,column=15)
        stoutput2=Label(frameinsert,text=" ",font=("Times New Roman", 10))
        stoutput2.grid(row=13,column=15)
        stoutput3=Label(frameinsert,text=" ",font=("Times New Roman", 10))
        stoutput3.grid(row=14,column=15)
        stoutput4=Label(frameinsert,text=" ",font=("Times New Roman", 10))
        stoutput4.grid(row=15,column=15)
        stoutput5=Label(frameinsert,text=" ",font=("Times New Roman", 10))
        stoutput5.grid(row=16,column=15)
        stoutput6=Label(frameinsert,text=" ",font=("Times New Roman", 10))
        stoutput6.grid(row=17,column=15)
        stoutput7=Label(frameinsert,text=" ",font=("Times New Roman", 10))
        stoutput7.grid(row=18,column=15)
        stoutput8=Label(frameinsert,text=" ",font=("Times New Roman", 10))
        stoutput8.grid(row=19,column=15)
        stoutput9=Label(frameinsert,text=" ",font=("Times New Roman", 10))
        stoutput9.grid(row=20,column=15)
    
    # Get Value :
        a=Name.get()
        b=Age.get()
        c=Tamil.get()
        d=English.get()
        e=Maths.get()
        f=Scince.get()
        g=S_Scince.get()
        e_con=MyDBConnection()
        result=e_con.cursor()
        statement="insert into Student_Mark_List(Name,Age,Tamil,English,Maths,Science,Social_Science) value(%s,22,%s,%s,%s,%s,%s);"
        # statement="insert into  Student_Mark_List(Name,Age) values(" + str(Name) + "," + str(Age) +");"
        valuepass=(a,b,c,d,e,f,g)
        result.execute(statement,valuepass)
        # print(statement)
        e_con.commit()
        msg=result.rowcount,"row Insert"
        stoutput2.config(text=a)
        # stoutput3.config(text=b)
        stoutput4.config(text=c)
        stoutput5.config(text=d)
        stoutput6.config(text=e)
        stoutput7.config(text=f)
        stoutput8.config(text=g)
        stoutput9.config(text=msg)

        
    
    
        details1.mainloop()
       

        
run=manuplate()
app.mainloop()