import mysql.connector 
from tkinter import *

class DBManipulate:
    
    def __init__(self):
        print("Welcome to Db Manipulation")

    def returnMsg(self):
        return "connected"
    
    def mydbconnection(self):
        con=mysql.connector.connect(
            host="192.168.1.240",
            user="AIBATCH01",
            password="AI@123",
            database="ai_saravanan"
        )
        return con
    
    def insertvalues(self,Name,age,tamil,english,maths,science,sscience):
        student_name=Name
        student_age=age
        st_mk_tam=tamil
        st_mk_eng=english
        st_mk_math=maths
        st_mk_sci=science
        st_mk_s_sci=sscience

        data=self.mydbconnection()
        result=data.cursor()

        stmts="insert into Student_Mark_List(Name,Age,Tamil,English,Maths,Science,Social_Science)  values(" +'"'+ student_name + '"' +","+ str(student_age) + "," + str(st_mk_tam) + ","+str(st_mk_eng) +"," + str(st_mk_math) + "," + str(st_mk_sci) + "," + str(st_mk_s_sci) + ");"
        result.execute(stmts)
        print(stmts)

        data.commit()

        return(str(result.rowcount)+"row Inserted")
    
    def updatevalue(self,S_no,Name,Age,Tamil,English,Maths,Science,sscience):
        # Assuming you have a database connection stored in self.connection
        # student_name=Name
        # student_age=age
        # st_mk_tam=tamil
        # st_mk_eng=english
        # st_mk_math=maths
        # st_mk_sci=science
        # st_mk_s_sci=sscience

        data1=self.mydbconnection()
        result1=data1.cursor()


        # Constructing SQL update statement with string concatenation
        update1 = (
            "UPDATE ai_saravanan.Student_Mark_List "
            "SET "
            "`S_no` = " + str(S_no) + ", "
            "`Name` = '" + Name + "', "
            "`age` = " + str(Age) + ", "
            "`tamil` = " + str(Tamil) + ", "
            "`English` = " + str(English) + ", "
            "`maths` = " + str(Maths) + ", "
            "`Science` = " + str(Science) + ", "
            "`Social_Science` = " + str(sscience) + " "
            "WHERE `S_no` = " + str(S_no)
        )

        # Create a cursor and execute the update query
        #cursor= self.DBconnection.cursor()
        result1.execute(update1)
        # print(update1)
        data1.commit()

        print(str(result1.rowcount)+"row Updated")


    def deletevalue(self,s_no):

        data2=self.mydbconnection()
        result2=data2.cursor()

        stmt1=(
            "delete from Student_Mark_List" 
           "WHERE `S_no` = " + str(s_no)
        )

        result2.execute(stmt1)
        print(stmt1)

        data2.commit()
        

